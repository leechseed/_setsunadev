# Security checklist (our words, from the public OWASP Top 10 categories)

Used by security-reviewer. Walk the categories against the files in scope; report only what you can point to with file:line.

## 1. The ten categories

1. **Injection.** Data reaching a shell, SQL string, eval, template or regex as code. Look for `shell=True`, `os.system`, f-string SQL, `eval`/`exec`. Fix: arg lists, `?` placeholders, no eval.
2. **Broken authentication.** Hardcoded or default passwords, tokens in URLs, no expiry, session files committed, weak comparison of secrets. Fix: env vars or a git-ignored file, constant-time compare.
3. **Sensitive data exposure.** Secrets, personal data or private detail in tracked files, logs, generated pages, error messages or git history. Plain-text storage of anything private. Fix: move to `_PRIVATE/`, redact, rotate anything that leaked.
4. **XXE and SSRF.** XML parsers that resolve external entities; code that fetches a URL taken from data (pages, PDFs, feeds) with no host allowlist or timeout. Fix: defusedxml or disable entities; allowlist hosts, block private ranges.
5. **Broken access control.** Local servers bound to all interfaces, endpoints with no check on who calls, paths built from data that can climb out with `..`. Fix: bind to 127.0.0.1, resolve the path and confirm it stays under the intended folder.
6. **Security misconfiguration.** Debug on, verbose errors, `verify=False`, open CORS, permissive file modes, unneeded services. See section 3.
7. **Cross-site scripting.** Generated HTML or JS that inserts untrusted text without escaping (innerHTML, string-built markup). Fix: `html.escape`, `textContent`.
8. **Insecure deserialization.** `pickle`, `yaml.load`, `marshal` or similar on files or data you did not make. Fix: `json`, `yaml.safe_load`.
9. **Known-vulnerable or unfamiliar dependencies.** Unpinned packages, abandoned libraries, packages installed from odd sources. Fix: pin, and run an audit tool only if already installed.
10. **Logging and monitoring gaps.** Secrets or private text written to logs; failures swallowed with no trace; no record of a destructive action. Fix: redact, log the event not the payload, never `except: pass`.

## 2. Differential review (read a diff for what it newly exposes)

Judge the change, not the whole codebase. For each hunk ask:

- **New inputs.** Any new file, argument, env var, form field, fetched page or message the code now reads? Treat each as untrusted until checked.
- **New network calls.** Any new host, URL or port, inbound or outbound? Where does the URL come from, and what is sent in it?
- **New file writes.** Any new path written, deleted or moved? Can data pick the path? Does it land in a tracked, public folder?
- **New privileges.** Any new subprocess, higher permission, wider bind address, relaxed check or added tool access?
- **Removed guards.** Was a validation, escape or check deleted or loosened?
- **History.** `git log -S` on touched lines: was this guard added to fix something earlier?

Report each as: what is newly reachable, from which input, and the smallest fix.

## 3. Insecure defaults

Flag any of these as shipped, not as configurable:

- Server or tool listening on `0.0.0.0`, or with no auth.
- Debug or verbose mode on by default.
- TLS verification off, or certificate errors ignored.
- Default or sample credentials, a blank password, a placeholder token that works.
- Fail-open: an error in a check lets the request through.
- Wildcard CORS, wildcard allowlists, world-writable files.
- Broad `except` that hides a failed security check.
- Secrets read from a tracked file when no env var is set.

Skip clearly marked placeholders in `.env.example` and test values.

## 4. Review prompt (confidence-gated pass)

Use this as the opening frame when the brief asks for a "high-confidence security review" of a diff. Rewritten in our words from the Anthropic `/security-review` prompt (OneRedOak/claude-code-workflows, MIT, Patrick Ellis). Source: https://raw.githubusercontent.com/OneRedOak/claude-code-workflows/main/security-review/security-review-slash-command.md

**Goal.** Find vulnerabilities the diff newly adds that someone could really exploit. This is not a general code review: ignore style, and ignore old problems the diff did not touch.

**Confidence bar.** Report a finding only if you are over 80% sure it can be exploited. Score each 1-10; drop anything below 8 on a second look. Skip theoretical, low-impact and style items. A local-network-only hole can still be high severity.

**Do not report:** denial of service or resource exhaustion; rate limiting; secrets that are already stored safely on disk (this repo's separate rule still applies: no secrets in tracked files); missing hardening with no concrete hole; theoretical races; outdated libraries; memory-safety talk in memory-safe languages; test-only files; markdown docs; log spoofing; regex injection or regex slowness; SSRF where only the path is controlled (host or scheme must be); missing audit logs; open redirects, tabnabbing and similar low-impact web items unless certain.

**Trusted inputs.** Environment variables and command-line flags are trusted. UUIDs are unguessable. Client-side code needs no auth checks; the server does. Shell scripts rarely take untrusted input: report only with a concrete attack path.

**Look for:** command, SQL, template and path-traversal injection; auth bypass and privilege escalation; hardcoded keys, weak crypto, certificate checks turned off; unsafe deserialization (pickle, yaml.load), eval, XSS; secrets or personal data in logs, errors or API output.

**Method.** (1) Learn the repo's existing safe patterns. (2) Compare the diff against them and flag departures and new attack surface. (3) Trace each input to each sensitive operation.

**Output per finding:** `file:line`, severity (high: remote code, data breach or auth bypass; medium: needs conditions but big impact, include only if obvious; low: defense-in-depth), category, what is wrong, an exploit scenario, the fix. Our severity words are in `severity.md`.

## 4. Threat model (before a tool or page goes public)

Write it in four short lists, each tied to files you read. Mark an assumption as an assumption.

- **Trust boundaries.** The edges where data crosses from one party or place to another: Chief to a script, a script to a fetched page, a local server to the browser, a private folder to a public one.
- **Assets.** What an attacker would want: credentials, private detail in `_PRIVATE/`, the repo history, the machine, the published pages.
- **Entry points.** Every place outside data gets in: arguments, fetched URLs, pasted text, parsed files, local ports, generated HTML.
- **Abuse paths.** For each: who does what to which asset through which entry point. Rate likelihood and impact low, medium or high, with one sentence of reason. Keep the list short; drop paths that need access the attacker does not have.

End with the two assumptions that move the ranking most, and the smallest fix for each high path.

<!-- structure informed by agamm/claude-code-owasp (MIT); differential-review idea only from trailofbits/skills, no text copied; threat-model section idea from openai/skills security-threat-model (license unconfirmed, no text copied) · BOLO 140 · 2026-10-13 -->
