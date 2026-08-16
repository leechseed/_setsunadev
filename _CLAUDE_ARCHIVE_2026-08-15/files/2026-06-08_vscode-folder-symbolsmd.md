---
original_path: "/mnt/user-data/outputs/vscode-folder-symbols.md"
source_conversation: "Valid symbols for folder names"
created: 2026-06-08
trunk: BLACK
kind: generated-file
---

# VSCode Valid Folder/File Name Symbols
## Alphabetical Sort Hierarchy

> Symbols that are valid on Windows and usable in VSCode, ordered by how a file explorer sorts them.

---

## Table of Contents

- [Full Hierarchy List](#full-hierarchy-list)
- [Excluded Symbols](#excluded-symbols)
- [Common Use Cases](#common-use-cases)

---

## Full Hierarchy List

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

---

## Excluded Symbols

| Symbol | Reason |
|--------|--------|
| ` ` (space) | Valid but sorts first and looks messy |
| `"` | Windows forbids it |
| `*` | Windows forbids it |
| `/` | Path separator — forbidden |
| `\` | Path separator — forbidden |
| `:` | Windows forbids it |
| `<` | Windows forbids it |
| `>` | Windows forbids it |
| `?` | Windows forbids it |
| `\|` | Windows forbids it |

---

## Common Use Cases

| Symbol | Position | Use Case |
|--------|----------|----------|
| `!` | Top | Absolute top priority folders |
| `#` | 2nd | Second tier pinning |
| `$` | 3rd | Third tier |
| `0–9` | After symbols | Numbered ordering |
| `_` | Near bottom | Common dev convention |
| `~` | Bottom | Push folder to the very bottom |

---

> **Note:** This list assumes Windows file system rules, which are the most restrictive.
> Valid on macOS and Linux as well (both allow more, but these are the safe cross-platform set).
