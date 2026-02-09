# ask_docs.py

import json
import os
import re
import subprocess
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

import numpy as np
import faiss
from rapidfuzz import fuzz
from sentence_transformers import SentenceTransformer

# Clipboard (optional)
try:
    import pyperclip  # type: ignore
    HAS_CLIPBOARD = True
except Exception:
    pyperclip = None
    HAS_CLIPBOARD = False


DOCS_JSONL = "docs.jsonl"
DOCS_INDEX = "docs.index"
OFFSETS_NPY = "docs.offsets.npy"


# ----------------------------
# Helpers
# ----------------------------

def load_config() -> dict:
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)


def norm_win_path(p: str) -> str:
    return os.path.normpath(p.replace("/", os.sep))


def copy_to_clipboard(s: str) -> None:
    if not HAS_CLIPBOARD:
        print("[err] Clipboard not available. In your ACTIVE venv: pip install pyperclip")
        return
    assert pyperclip is not None
    pyperclip.copy(s)
    print("[ok] Copied to clipboard.")


def open_in_editor(path: str) -> None:
    path = norm_win_path(path)
    if not os.path.exists(path):
        print(f"[err] file not found: {path}")
        return

    for cmd in ("code", "code.cmd"):
        try:
            subprocess.run(
                [cmd, "--reuse-window", path],
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print(f"[ok] Opened in VS Code: {path}")
            return
        except Exception:
            pass

    try:
        os.startfile(path)
        print(f"[ok] Opened in default app: {path}")
    except Exception as e:
        print(f"[err] couldn't open file: {e}")


def read_entire_file(path: str) -> str:
    path = norm_win_path(path)
    try:
        return open(path, "r", encoding="utf-8").read()
    except Exception:
        try:
            return open(path, "r", encoding="utf-8", errors="ignore").read()
        except Exception:
            return "[err] Could not read file."


# ----------------------------
# Fast random access for docs.jsonl (scale)
# ----------------------------

def build_or_load_offsets(jsonl_path: str, offsets_path: str) -> np.ndarray:
    """
    Creates or loads byte-offset index. 
    RE-BUILDS if the jsonl file is newer than the offsets file.
    """
    exists = os.path.exists(offsets_path)
    
    # Check if we need to force a rebuild because the source file changed
    if exists:
        if os.path.getmtime(jsonl_path) > os.path.getmtime(offsets_path):
            print("[build] docs.jsonl updated, rebuilding offsets...")
            exists = False

    if exists:
        return np.load(offsets_path, allow_pickle=False)

    print("[build] creating docs.offsets.npy (one-time)…")
    offsets: List[int] = []
    off = 0

    with open(jsonl_path, "rb") as f:
        for line in f:
            offsets.append(off)
            off += len(line)

    arr = np.asarray(offsets, dtype=np.int64)
    np.save(offsets_path, arr, allow_pickle=False)
    print(f"[build] offsets ready: {len(arr)} lines")
    return arr


def read_doc_by_id(jsonl_path: str, offsets: np.ndarray, doc_id: int) -> dict:
    """
    Random access read of a single JSONL line by FAISS id.
    """
    if doc_id < 0 or doc_id >= len(offsets):
        # Return a dummy dict rather than crashing everything
        return {"text": f"[Error: ID {doc_id} out of bounds]", "meta": {"path": "N/A", "chunk_index": 0}}

    with open(jsonl_path, "rb") as f:
        f.seek(int(offsets[doc_id]))
        line = f.readline()

    try:
        return json.loads(line.decode("utf-8", errors="ignore"))
    except Exception:
        return {"text": "[Error: JSON decode failed]", "meta": {"path": "N/A", "chunk_index": 0}}


# ----------------------------
# Scoring (accuracy)
# ----------------------------

TOKEN_RE = re.compile(r"[a-z0-9_]+")

def tokenize(s: str) -> List[str]:
    return TOKEN_RE.findall(s.lower())


def keyword_score(query: str, text: str) -> float:
    q = query.strip().lower()
    t = text.lower()
    if not q or not t: return 0.0

    if q in t:
        base = 0.85
    else:
        base = 0.0

    q_tokens = tokenize(q)
    if not q_tokens:
        return max(base, fuzz.partial_ratio(q, t) / 100.0)

    t_tokens = set(tokenize(t))
    if not t_tokens: return base

    overlap = sum(1 for tok in q_tokens if tok in t_tokens)
    overlap_ratio = overlap / max(1, len(set(q_tokens)))
    fuzzy = fuzz.partial_ratio(q, t) / 100.0
    kw = (overlap_ratio * 0.65) + (fuzzy * 0.35)

    return max(base, kw)


def hybrid_score(vec: float, kw: float, query: str) -> float:
    qt = tokenize(query)
    n = len(qt)
    if n <= 2:
        w_vec, w_kw = 0.65, 0.35
    elif n <= 6:
        w_vec, w_kw = 0.75, 0.25
    else:
        w_vec, w_kw = 0.82, 0.18
    return (vec * w_vec) + (kw * w_kw)


def format_hit(rank: int, score: float, vec: float, kw: float, doc: dict, max_chars: int = 1300) -> str:
    path = doc.get("meta", {}).get("path", "Unknown")
    chunk_idx = doc.get("meta", {}).get("chunk_index", 0)
    text = doc.get("text", "")

    excerpt = text.strip()
    if len(excerpt) > max_chars:
        excerpt = excerpt[:max_chars].rstrip() + "\n…"

    out = []
    out.append(f"[{rank}] score={score:.3f} (vec={vec:.3f}, kw={kw:.3f})")
    out.append(f"FILE: {path}")
    out.append(f"CHUNK: {chunk_idx}")
    out.append("-" * 90)
    out.append(excerpt)
    out.append("")
    return "\n".join(out)


# ----------------------------
# Main loop
# ----------------------------

@dataclass
class Hit:
    score: float
    vec: float
    kw: float
    doc_id: int
    doc: dict


def main():
    cfg = load_config()
    top_k = int(cfg.get("top_k", 6))
    min_score = float(cfg.get("min_score", 0.15))
    fetch_k = int(cfg.get("fetch_k", max(60, top_k * 25)))
    group_by_file = bool(cfg.get("group_by_file", True))

    if not os.path.exists(DOCS_INDEX):
        raise SystemExit(f"Missing {DOCS_INDEX}. Run indexer first.")
    if not os.path.exists(DOCS_JSONL):
        raise SystemExit(f"Missing {DOCS_JSONL}. Run indexer first.")

    offsets = build_or_load_offsets(DOCS_JSONL, OFFSETS_NPY)
    index = faiss.read_index(DOCS_INDEX)
    model = SentenceTransformer(cfg["model_name"])

    last_formatted = ""
    last_rank_to_doc = {}

    print("\nReady.")
    print("Commands: :quit, :copy, :open N, :path N, :file N, :k=N, :min=N, :fetch=N, :group=on/off\n")

    while True:
        try:
            q = input("ask> ").strip()
        except EOFError:
            break
            
        if not q: continue
        qlow = q.lower()

        if qlow in {":quit", "quit", "exit"}:
            break

        # --- Command Handling ---
        if q.startswith(":k="):
            try:
                top_k = int(q.split("=", 1)[1])
                print(f"[ok] top_k={top_k}")
            except: print("[err] use :k=10")
            continue

        if q.startswith(":min="):
            try:
                min_score = float(q.split("=", 1)[1])
                print(f"[ok] min_score={min_score}")
            except: print("[err] use :min=0.20")
            continue

        if q == ":copy":
            if not last_formatted.strip(): print("[err] No results yet.")
            else: copy_to_clipboard(last_formatted)
            continue

        if q.startswith(":open "):
            try:
                n = int(q.split(" ", 1)[1].strip())
                doc = last_rank_to_doc.get(n)
                if doc: open_in_editor(doc["meta"].get("path", ""))
                else: print("[err] Invalid hit number.")
            except: print("[err] use :open 1")
            continue

        if q.startswith(":path "):
            try:
                n = int(q.split(" ", 1)[1].strip())
                doc = last_rank_to_doc.get(n)
                if doc: copy_to_clipboard(norm_win_path(doc["meta"].get("path", "")))
            except: print("[err] use :path 1")
            continue

        if q.startswith(":file "):
            try:
                n = int(q.split(" ", 1)[1].strip())
                doc = last_rank_to_doc.get(n)
                if doc: copy_to_clipboard(read_entire_file(doc["meta"].get("path", "")))
            except: print("[err] use :file 1")
            continue

        # --- Search Execution ---
        qv = model.encode([q], normalize_embeddings=True).astype("float32")
        D, I = index.search(qv, max(fetch_k, top_k * 10))

        hits: List[Hit] = []
        for vec, doc_id in zip(D[0], I[0]):
            if doc_id == -1: continue
            
            # Safety Check for doc_id range
            if doc_id >= len(offsets):
                continue

            doc = read_doc_by_id(DOCS_JSONL, offsets, int(doc_id))
            kw = keyword_score(q, doc.get("text", ""))
            score = hybrid_score(float(vec), float(kw), q)
            hits.append(Hit(score=score, vec=float(vec), kw=float(kw), doc_id=int(doc_id), doc=doc))

        hits.sort(key=lambda h: h.score, reverse=True)

        selected: List[Hit] = []
        seen_files = set()

        for h in hits:
            if h.score < min_score: continue
            if group_by_file:
                f = h.doc.get("meta", {}).get("path", "")
                if f and f in seen_files: continue
                if f: seen_files.add(f)
            selected.append(h)
            if len(selected) >= top_k: break

        print()
        if not selected:
            last_formatted = ""
            last_rank_to_doc = {}
            print("No strong matches found.\n")
            continue

        formatted_blocks = []
        last_rank_to_doc = {}

        for rank, h in enumerate(selected, start=1):
            block = format_hit(rank, h.score, h.vec, h.kw, h.doc)
            print(block)
            formatted_blocks.append(block)
            last_rank_to_doc[rank] = h.doc

        last_formatted = "\n".join(formatted_blocks)
        print("Tip: :copy | :file N | :open N\n")

if __name__ == "__main__":
    main()


# index_docs.py

import json
import os
import re
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# ----------------------------
# Logging Setup
# ----------------------------
logging.basicConfig(
    filename='indexing.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

DEFAULT_STRIP_FRONTMATTER_KEYS = {
    "updated", "created", "latitude", "longitude", "altitude", "author",
    "source_url", "is_todo", "todo_due", "todo_completed", "source",
    "source_application", "application_data", "order", "user_created_time",
    "user_updated_time", "encryption_cipher_text", "encryption_applied",
    "markup_language", "is_shared", "share_id", "conflict_original_id",
    "master_key_id", "user_data", "deleted_time", "type_",
}

FM_RE = re.compile(r"\A(?:\ufeff)?\s*---\s*\n(.*?)\n---\s*\n", re.S)
TAG_IN_BODY_RE = re.compile(r"(?<!\w)#([A-Za-z0-9_\-\/]+)")
INLINE_TAGS_RE = re.compile(r"(?im)^\s*tags\s*::\s*(.+?)\s*$")

def load_config() -> dict:
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def read_text(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except Exception:
        try:
            return Path(path).read_text(encoding="utf-8", errors="ignore")
        except:
            return ""

def parse_front_matter(text: str) -> Tuple[Dict[str, object], str]:
    m = FM_RE.match(text)
    if not m: return {}, text
    fm_block = m.group(1)
    body = text[m.end():]
    fm = simple_yaml_parse(fm_block)
    return fm, body

def simple_yaml_parse(block: str) -> Dict[str, object]:
    out = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^([A-Za-z0-9_\-]+)\s*:\s*(.*)$", line)
        if m:
            key, rest = m.group(1).strip(), m.group(2).strip()
            out[key] = rest.strip("'\"")
        i += 1
    return out

def normalize_tags(fm: Dict[str, object]) -> List[str]:
    t = fm.get("tags", [])
    if isinstance(t, str): return [x.strip().lower() for x in t.split(",") if x.strip()]
    if isinstance(t, list): return [str(x).lower() for x in t]
    return []

def extract_tags_from_body(body: str) -> List[str]:
    return [t.lower() for t in TAG_IN_BODY_RE.findall(body)]

def chunk_text(text: str, chunk_chars: int, overlap: int) -> List[str]:
    s = text.strip()
    chunks, start, n = [], 0, len(s)
    while start < n:
        end = min(start + chunk_chars, n)
        chunks.append(s[start:end].strip())
        if end >= n: break
        start = max(0, end - overlap)
    return chunks

@dataclass
class DocChunk:
    text: str
    meta: dict

def main():
    cfg = load_config()
    source_root = Path(cfg["source_dir"])
    include_folders = cfg.get("include_folders", [])
    
    # Pre-cleanup
    for f in ["docs.index", "docs.offsets.npy", "docs.jsonl"]:
        if os.path.exists(f): os.remove(f)

    print(f"--- Scanning {source_root} ---")
    all_files = list(source_root.rglob("*.md"))
    
    # Filtering logic for include_folders
    if include_folders:
        filtered_files = []
        for p in all_files:
            # Check if any folder in the path matches our whitelist
            if any(folder in p.parts for folder in include_folders):
                filtered_files.append(p)
        md_files = filtered_files
    else:
        md_files = all_files

    chunks = []
    model_name = cfg.get("model_name", "all-MiniLM-L6-v2")
    chunk_chars = int(cfg.get("chunk_chars", 1200))
    chunk_overlap = int(cfg.get("chunk_overlap", 150))

    for path in tqdm(md_files, desc="Indexing", unit="file"):
        raw = read_text(str(path))
        if not raw: continue
        fm, body = parse_front_matter(raw)
        tags = normalize_tags(fm)
        if cfg.get("include_body_hashtags"): tags += extract_tags_from_body(body)
        
        indexed_text = (f"TAGS: {', '.join(tags)}\n\n" + body).strip()
        file_chunks = chunk_text(indexed_text, chunk_chars, chunk_overlap)
        
        for idx, c_text in enumerate(file_chunks):
            chunks.append(DocChunk(text=c_text, meta={"path": str(path).replace("\\", "/"), "chunk_index": idx, "tags": tags}))

    if not chunks:
        print("No files found. Check include_folders in config.")
        return

    print(f"--- Embedding {len(chunks)} chunks ---")
    model = SentenceTransformer(model_name)
    vecs = model.encode([c.text for c in chunks], normalize_embeddings=True, show_progress_bar=True)
    
    faiss.write_index(faiss.IndexFlatIP(vecs.shape[1]), "docs.index")
    index = faiss.read_index("docs.index")
    index.add(np.asarray(vecs, dtype="float32"))
    faiss.write_index(index, "docs.index")

    with open("docs.jsonl", "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps({"text": c.text, "meta": c.meta}, ensure_ascii=False) + "\n")

    print(f"DONE. Indexed {len(md_files)} files.")

if __name__ == "__main__":
    main()



