---
title: "Valid symbols for folder names"
uuid: 17432d9c-887a-4189-952d-93b395d21712
created: 2026-06-08
updated: 2026-06-08
trunk: BLACK
messages: 8
chars: 3458
artifacts: 0
generated_files: 1
tools: [create_file, present_files]
source: claude.ai-export-2026-08-15
---

# Valid symbols for folder names

> **Conversation Overview**

The person asked a series of questions about valid symbols for file and folder names, focusing on cross-platform compatibility and how symbols sort alphabetically in file explorers. The conversation progressed from a general overview of OS-specific restrictions (Windows, macOS, Linux) to a focused, practical list of symbols valid specifically for use in VSCode on Windows. Key topics included ASCII sort order hierarchy, which symbols are forbidden on Windows, and how symbols can be used strategically to control folder ordering in a file explorer.

The person then requested the final reference information be formatted as a markdown file, which Claude created as a downloadable artifact. The markdown document included a full hierarchy list of valid symbols in sort order, a table of excluded symbols with reasons, and a common use cases table showing how specific symbols like `!`, `#`, `$`, `_`, and `~` can be used to pin or push folders to the top or bottom of a directory listing. The person's communication style was direct and iterative, refining the scope of the request step by step from broad OS rules down to a specific, actionable VSCode-ready reference document.

**Files produced**

- [vscode-folder-symbols.md](../files/2026-06-08_vscode-folder-symbolsmd.md)

---
## 🧑 Papi  <sub>2026-06-08 01:24:22</sub>

what symbols are valid for file folder titles

---

## 🤖 Claude  <sub>2026-06-08 01:24:29</sub>

In most operating systems, the rules are:

**Windows** is the most restrictive — these characters are **not allowed** in file/folder names:
`\ / : * ? " < > |`

**macOS** forbids only:
`: /`

**Linux** forbids only:
`/` (null byte technically also invalid, but rarely relevant)

---

**Safe everywhere** (cross-platform): alphanumerics, spaces, hyphens `-`, underscores `_`, periods `.`, and parentheses `()`.

**Generally safe but use with caution:** `[ ] { } ! @ # $ % ^ & ~ ' + =`

**Avoid even if technically allowed:** leading/trailing spaces or periods (Windows strips them), names like `CON`, `PRN`, `AUX`, `NUL`, `COM1-9`, `LPT1-9` on Windows (reserved device names).

If you're naming Obsidian vault folders specifically — all of the above applies, plus Obsidian uses `[[` `]]` for wikilinks so brackets in filenames can cause weirdness. Stick to alphanumerics, spaces, hyphens, underscores, and periods for maximum compatibility across vaults and sync tools.

---

## 🧑 Papi  <sub>2026-06-08 01:25:02</sub>

ok if i were to sort by alfa order what would be the higherarchy for symbals

---

## 🤖 Claude  <sub>2026-06-08 01:25:10</sub>

Alphabetical/ASCII sort order goes:

**Spaces first**, then symbols, then numbers, then uppercase letters, then lowercase letters.

Symbol order (roughly, by ASCII value):
```
(space)
! " # $ % & ' ( ) * + , - . /
0–9
: ; < = > ? @
A–Z
[ \ ] ^ _  `
a–z
{ | } ~
```

So in a file explorer sorting alphabetically:

1. Space ` `
2. `!`
3. `"`
4. `#`
5. `$`
6. `%`
7. `&`
8. `'`
9. `(`
10. `)`
11. `*`
12. `+`
13. `,`
14. `-`
15. `.`
16. `/` *(not usable in names)*
17. `0–9`
18. `:` *(restricted on Windows/Mac)*
19. `@`
20. `A–Z`
21. `[`
22. `]`
23. `^`
24. `_`
25. `` ` ``
26. `a–z`
27. `{`
28. `|`
29. `}`
30. `~`

---

**Practical takeaway for forcing folders to the top in Obsidian or any file explorer:**

- `!` or `_` prefix = near top
- `0` prefix = after symbols, before letters
- Most people use `!` or `_` to pin important folders above everything else

---

## 🧑 Papi  <sub>2026-06-08 01:27:36</sub>

ok i like this. give me all the ones in a list higherarchaly that i can use in vscode

---

## 🤖 Claude  <sub>2026-06-08 01:27:42</sub>

Here's what's valid in folder/file names that VSCode (on Windows) will accept, in sort order:

```
!
#
$
%
&
'
(
)
+
,
-
.
0–9
;
=
@
A–Z
[
]
^
_
`
a–z
{
}
~
```

**Excluded:**
- `space` — valid but sorts first and looks messy
- `"` — Windows forbids it
- `*` — Windows forbids it
- `/` — path separator, forbidden
- `\` — path separator, forbidden
- `:` — Windows forbids it
- `<` — Windows forbids it
- `>` — Windows forbids it
- `?` — Windows forbids it
- `|` — Windows forbids it

---

**Most commonly used for sorting/organization:**

| Symbol | Use case |
|--------|----------|
| `!` | Absolute top priority folders |
| `#` | Second tier pinning |
| `$` | Third tier |
| `0–9` | Numbered ordering |
| `_` | Underscore prefix (common dev convention) |
| `~` | Push to bottom |

---

## 🧑 Papi  <sub>2026-06-08 01:28:03</sub>

give this to me in a markdown

---

## 🤖 Claude  <sub>2026-06-08 01:28:19</sub>

Here's the markdown file:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

There you go — knowledgebase-ready with a TOC and tables.