// zlib_favorites_walker.js — extract full Z-lib favorites list across all pages
// USAGE: log in, open the FAVORITES page, F12 → Console, paste entire script, Enter.
// Walks pagination as your session (credentials:include), 0.8s delay per page,
// auto-downloads `zlib-favorites.txt` (one "Author — Title" per line).
// Then: move file to Desktop\_BVX_INBOX\zlib\ and tell Claude "go" →
// parser + fuzzy-diff against _0.1_BVX_LEARN/_meta/catalog.json (1,106 sources)
// → three lists: already-catalogued / THE GAP (acquisition queue) / review-queue maybes.
// If it stalls at "page 2: +0": that mirror paginates differently — capture the
// next-page URL from the address bar and re-cut the `page=` param logic to match.

(async () => {
  const seen = new Set(), out = [];
  const grab = (doc) => {
    let n = 0;
    doc.querySelectorAll('z-bookcard').forEach(b => {
      const t = b.getAttribute('title') || b.querySelector('[slot="title"]')?.textContent?.trim();
      const a = b.getAttribute('author') || b.querySelector('[slot="author"]')?.textContent?.trim() || '?';
      if (t && !seen.has(a + t)) { seen.add(a + t); out.push(`${a} — ${t}`); n++; }
    });
    if (n === 0) doc.querySelectorAll('h3 a, .book-title, td .title a').forEach(x => {
      const t = x.textContent.trim();
      if (t && !seen.has(t)) { seen.add(t); out.push(t); n++; }
    });
    return n;
  };
  grab(document);
  let url = location.href.replace(/([?&])page=\d+/, ''), page = 2, added = 1;
  const sep = url.includes('?') ? '&' : '?';
  while (added > 0 && page < 200) {
    const r = await fetch(`${url}${sep}page=${page}`, { credentials: 'include' });
    if (!r.ok) break;
    const doc = new DOMParser().parseFromString(await r.text(), 'text/html');
    added = grab(doc);
    console.log(`page ${page}: +${added} (total ${out.length})`);
    page++;
    await new Promise(s => setTimeout(s, 800));
  }
  const blob = new Blob([out.join('\n')], { type: 'text/plain' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'zlib-favorites.txt';
  a.click();
  console.log(`DONE: ${out.length} books → zlib-favorites.txt`);
})();
