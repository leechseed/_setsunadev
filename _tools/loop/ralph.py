#!/usr/bin/env python
"""Ralph loop (BOLO 140): run `claude -p` with a fixed prompt until a done-check passes.

usage: python _tools/loop/ralph.py <job.json> [--max N] [--dry]
Stdlib only. Never deletes, never reverts, never pushes. Stops and reports.
"""
import argparse, datetime, fnmatch, json, os, shutil, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP_DIR = "_tools/loop/"  # the loop's own logs are never "changed files"


def sh(cmd):
    p = subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def dirty():
    p = subprocess.run(["git", "status", "--porcelain", "-uall"], cwd=ROOT, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    out = {}
    for line in p.stdout.splitlines():
        if len(line) > 3:
            path = line[3:].strip().strip('"')
            if " -> " in path:
                path = path.split(" -> ")[1]
            out[path] = line[:2]
    return out


def allowed(path, globs):
    return any(fnmatch.fnmatch(path, g) for g in globs)


def usage_tokens(res):
    u = res.get("usage") or {}
    return sum(int(u.get(k) or 0) for k in
               ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("job")
    ap.add_argument("--max", type=int)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    job = json.load(open(a.job, encoding="utf-8"))
    name = os.path.splitext(os.path.basename(a.job))[0]
    mx = a.max or int(job.get("max_iterations", 5))
    budget = int(job.get("token_budget", 0)) or None
    stop_file = os.path.join(ROOT, job.get("stop_file", "_tools/loop/ABORT"))
    globs = job.get("allowed_paths", [])
    prompt = open(os.path.join(ROOT, job["prompt_file"]), encoding="utf-8").read()
    log = os.path.join(ROOT, "_tools/loop/runs", f"{name}-{datetime.date.today().isoformat()}.jsonl")
    claude = shutil.which("claude")
    cmd_tpl = ["claude", "-p", "<prompt + check output>", "--output-format", "json",
               "--max-turns", "15", "--permission-mode", "acceptEdits"]

    if a.dry:
        print(f"DRY · job {name} · max {mx} · budget {budget} · claude={claude}")
        print(f"cwd: {ROOT}\nlog: {log}\nallowed: {globs}")
        for i in range(1, mx + 1):
            print(f"[iter {i}] 1. if exists {stop_file}: STOP")
            print(f"[iter {i}] 2. run done_cmd: {job['done_cmd']}  (exit 0 -> DONE)")
            print(f"[iter {i}] 3. run: {' '.join(cmd_tpl)}  (prompt = {job['prompt_file']} + last check output)")
            print(f"[iter {i}] 4. git status --porcelain: file outside allowed -> NO-GO, stop (no revert)")
            print(f"[iter {i}] 5. append JSON line to log; stop if usage sum > {budget}")
        return 0

    if not claude:
        print("NO-GO · claude not on PATH")
        return 2
    os.makedirs(os.path.dirname(log), exist_ok=True)
    baseline = dirty()
    total = 0
    last = ""
    for i in range(1, mx + 1):
        if os.path.exists(stop_file):
            print(f"ABORT · stop file present before iteration {i}")
            return 3
        code, last = sh(job["done_cmd"])
        if code == 0:
            print(f"DONE · check passed before iteration {i} · tokens {total}")
            print(last.strip().splitlines()[-1] if last.strip() else "")
            return 0
        print(f"[iter {i}] check exit {code}; running claude")
        full = f"{prompt}\n\nThe check output was:\n{last}"
        t0 = time.time()
        p = subprocess.run([claude, "-p", full, "--output-format", "json", "--max-turns", "15",
                            "--permission-mode", "acceptEdits"], cwd=ROOT, capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
        secs = round(time.time() - t0, 1)
        try:
            res = json.loads(p.stdout)
        except Exception:
            res = {"raw": (p.stdout or "")[:500], "stderr": (p.stderr or "")[:500]}
        toks = usage_tokens(res)
        total += toks
        now = dirty()
        changed = sorted(f for f, s in now.items() if baseline.get(f) != s and not f.startswith(LOOP_DIR))
        bad = [f for f in changed if not allowed(f, globs)]
        rec = {"iteration": i, "seconds": secs, "claude_exit": p.returncode, "usage": res.get("usage"),
               "tokens": toks, "cost_usd": res.get("total_cost_usd"), "files_changed": changed,
               "done_cmd_exit_before": code, "result": str(res.get("result", res.get("raw", "")))[:400]}
        with open(log, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec) + "\n")
        print(f"[iter {i}] {secs}s · tokens {toks} · changed {changed}")
        if p.returncode != 0 and "usage" not in res:
            print(f"NO-GO · claude failed: {rec['result']} {res.get('stderr','')}")
            return 2
        if bad:
            print(f"NO-GO · files changed outside allowed paths: {bad} (nothing reverted)")
            return 4
        if budget and total > budget:
            print(f"STOP · token budget passed ({total} > {budget})")
            return 5
    code, last = sh(job["done_cmd"])
    print(("DONE" if code == 0 else "CAP") + f" · after {mx} iterations · check exit {code} · tokens {total}")
    print(last.strip().splitlines()[-1] if last.strip() else "")
    return 0 if code == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
