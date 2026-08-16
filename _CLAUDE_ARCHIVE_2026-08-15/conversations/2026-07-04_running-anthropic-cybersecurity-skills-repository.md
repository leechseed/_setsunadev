---
title: "Running Anthropic cybersecurity skills repository"
uuid: c0dc305c-13a2-4a43-baf4-62a18db26124
created: 2026-07-04
updated: 2026-07-04
trunk: ORANGE
messages: 6
chars: 25596
artifacts: 0
generated_files: 3
tools: [bash_tool, create_file, present_files, view, web_fetch, web_search]
source: claude.ai-export-2026-08-15
---

# Running Anthropic cybersecurity skills repository

> **Conversation Overview**

The person wanted to quickly set up and use a GitHub repository called `mukul975/Anthropic-Cybersecurity-Skills` with Claude Code, communicating in a direct, fast-moving style and explicitly stating they needed to start a project immediately. The conversation moved from explanation of what the repo actually is, to a walkthrough of installation options, to Claude building a complete working scaffold when the person indicated they just needed something functional fast.

Claude investigated the repository hands-on throughout: cloning it, inspecting its real structure (817 skills organized in flat folders under `skills/`, each containing a `SKILL.md` with YAML frontmatter, `references/` documentation, and a functional `scripts/agent.py` of 150–260 lines), parsing subdomain categories from frontmatter, and selecting a curated defensive starter set of 27 skills across domains including incident response, threat hunting, digital forensics, SOC operations, malware analysis, network security, cloud security, vulnerability management, endpoint security, phishing defense, and ransomware defense.

The deliverable was three tested files: `setup.sh` (a shell script that clones the source repo once into `.cache/`, installs skills into `.claude/skills/` project-scoped, and supports `--list`, `--domain <name>`, and `--all` flags), `CLAUDE.md` (project context file Claude Code auto-loads to prime the agent as a defensive DFIR assistant with guardrails around authorization, script review, and malware handling), and `README.md` (quickstart documentation). The script was functionally verified against the live repo in a sandbox. Claude consistently flagged that the repo is a community project unaffiliated with Anthropic despite its name, and that the `agent.py` scripts are real runnable Python that should be reviewed before execution, especially for offensive-category skills. The person's preference is clearly for speed and concrete output over detailed explanation.

**Files produced**

- [setup.sh](../files/2026-07-04_setupsh.md)
- [CLAUDE.md](../files/2026-07-04_claudemd.md)
- [README.md](../files/2026-07-04_readmemd.md)

---
## 🧑 Papi  <sub>2026-07-04 08:20:35</sub>

lets run this https://github.com/mukul975/Anthropic-Cybersecurity-Skills

---

## 🤖 Claude  <sub>2026-07-04 08:21:39</sub>

I'm looking at a GitHub repository URL that claims to be about Anthropic Cybersecurity Skills, but I need to verify what it actually contains before proceeding. I'm being cautious here since the name suggests an affiliation with Anthropic, and I should check for any potential security concerns or malicious code before running anything from it.
```
This block is not supported on your current device yet.
```

Looking at this repository, it's a community-maintained cybersecurity skills library for AI agents with nearly 10k stars and a large collection of Python-based tools. The user wants to "run this," but since it's a skills library rather than a standalone application, I need to figure out what they actually mean—likely they want to install and use it, possibly through a package manager like npm.

I'm also noticing this library includes offensive security content like penetration testing and red teaming, which touches on areas I need to be careful about. However, it's a legitimate, widely-used open-source educational resource that maps to standard security frameworks like MITRE ATT&CK and NIST CSF, so it's primarily defensive in nature. I should flag to the user that despite the name, this isn't actually affiliated with Anthropic—it just uses their name in the title.

The ambiguity here is what "run" means in this context. I have access to bash tools and network connectivity to GitHub, so I could clone the repository into my sandbox environment, but that wouldn't accomplish much without understanding what the user actually wants to do with it. them, but I can clone it to show them the structure and content. The real question is whether they want to explore it locally or understand what's inside first — executing random Python scripts from an untrusted repo without knowing their purpose isn't the right move, so I should clarify their intent before diving in. I'm confirming this is a legitimate security education resource—blue-team defensive material, not offensive exploit code—so helping them explore or install it is straightforward. Given their casual, direct communication style, I should match that tone and lead with the key clarification: this isn't an Anthropic project despite the name, it's a community library of security playbooks meant to be installed into an agent on their own machine, not something I can run in my sandbox.Quick heads up before we touch it: despite the name, this isn't an Anthropic project. It's a community repo by one person (mukul975 / Mahipal Jangra) — it says so right at the top and bottom of the README ("Not affiliated with Anthropic PBC"). The "Anthropic" in the title is basically brand-borrowing for reach. It's Apache-2.0, ~9.6k stars, legit and widely indexed — just not official.

The other thing: there's no real "run" here. It's not an app. It's 754 Markdown skill files (`SKILL.md` + YAML frontmatter, plus some Python helper scripts) meant to be *loaded by an agent* so it has security playbooks to follow — threat hunting, forensics, DFIR, pentest workflows, all mapped to MITRE ATT&CK / NIST / etc. The actual "use it" step is installing it into your agent, which happens on your machine, not in my sandbox:

```
# into a Claude Code / agentskills.io-compatible setup
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# or just pull the files
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
```

So what are you actually after? Two things I can do right now:

- **Clone it into my sandbox and give you a real rundown** — structure, a couple sample skills opened up, and an honest read on whether the content is substantive or just AI-generated filler dressed up with framework tags. (I'd read the files, not blind-run the Python scripts.)
- **Walk you through wiring it into Claude Code** (or Cursor / whatever you're running) so it actually loads and your agent can pull from it.

Which way do you want to go?

---

## 🧑 Papi  <sub>2026-07-04 08:22:23</sub>

Walk you through wiring it into Claude Code

---

## 🤖 Claude  <sub>2026-07-04 08:24:52</sub>

I'm thinking through how to accurately explain integrating this cybersecurity skills repo with Claude Code, making sure I get the details right about how skills work in Claude Code and the specific installation process for this repository. I need to verify the exact installation method from the repo's README and check what Claude Code's current skills mechanism looks like, since the product-self-knowledge skill might cover Claude Code specifics but probably won't detail the skills directory structure. Let me fetch both the repo README and check the product-self-knowledge skill to get accurate information about how these 754 skills integrate with Claude Code.Good choice — that's the more useful path anyway since you keep control over what actually lands in your setup. Let me pull the exact install method from the repo and confirm the current Claude Code skills mechanism so I'm not handing you stale commands.
```
This block is not supported on your current device yet.
```

I need to check the Claude Code documentation for the skills mechanism and grab the exact installation instructions from the repository's README.
```
This block is not supported on your current device yet.
```

I need to fetch the GitHub repository page directly and extract the README content to access the information I'm looking for.
```
This block is not supported on your current device yet.
```

Looking at the README, this is set up as a Claude Code plugin with a `.claude-plugin` directory, and it can be installed either through the agentskills.io CLI or by cloning the repo directly. The project contains 754 skills organized across 26 domains, with each skill structured as a folder containing documentation, reference materials, processing scripts, and assets.

Now I'm thinking through how skills actually get wired into Claude Code — there are multiple installation paths including personal skills directories, project-level skills, the marketplace plugin mechanism, and third-party CLI tools. I want to make sure I'm giving accurate information about the current Claude Code skills architecture, so I should verify the official documentation to confirm the exact mechanisms and any recent changes. I should search for the current Claude Code documentation to verify the exact paths and commands for skills and plugins.Got it — I've got the repo structure and the exact install paths. One thing worth confirming against current docs (the skills/plugin mechanism in Claude Code has moved fast), then I'll give you the walkthrough.
```
This block is not supported on your current device yet.
```

I'm looking at the official documentation for Claude's code skills mechanism, which shows how skills are organized across personal, project, and plugin contexts using specific directory structures.

The repo itself is packaged as a Claude Code plugin with 754 skills total — a massive collection that presents practical challenges around token usage and skill discovery, so selectively loading skills rather than everything at once would be more efficient in practice.

Since these skills include process.py helper scripts that can execute code, especially in security-focused domains like red teaming and penetration testing, it's worth reviewing what scripts might run before letting an agent execute them automatically, ideally in a scoped or sandboxed project.

The repo has some promotional elements baked in (sponsorships, badges, growth-focused naming), which is worth noting given the "Anthropic" branding is community-driven rather than official.

For wiring this into Claude Code, the cleanest approach is using the plugin marketplace since the repo ships with the necessary plugin configuration — adding the marketplace source and then browsing available skills to install at either user or project scope. I'm settling on the conversational walkthrough approach since they asked me to walk them through it, not create a doc — though I can offer a markdown reference afterward if they want to keep it. I'll structure this around three installation routes: the one-liner for speed, the git clone method for control, and the plugin marketplace approach, each with its tradeoffs. The key insight is that they care about avoiding context bloat and maintaining visibility into what gets installed, so I'll lead with the selective install path and flag the gotchas around script execution and scope. I'm verifying the command syntax against the official docs and recent sources — `npx skills add` is the agentskills.io CLI, the `/plugin marketplace` route depends on marketplace.json existing, and the `.claude/skills/` paths are confirmed. I'm also noting that the MindStudio reference to `.claude/commands/` is outdated. On the policy side, helping someone install a dual-use security framework in their own agent is fine — the content is practitioner-oriented (detection, forensics, hardening) with standard pentest playbooks, and I should flag the script-review step as good security hygiene for any third-party repo, not gatekeeping.

Now I'm mapping out the actual installation paths: cloning the repo and cherry-picking specific skill folders into `~/.claude/skills/`, or bulk-copying all 754 skills with a tradeoff note. I'm also clarifying that the repo supports both native plugin installation via `.claude-plugin/` and manual skill folder placement, giving the user three routes from fastest to most selective. I'll steer toward the selective approach and explain the reasoning. The big caveat is that 754 skills is overwhelming—even just the metadata adds 20k+ tokens to every task, which clutters unrelated projects. Unless you're building a dedicated security agent, I'd scope it to a project directory or cherry-pick specific domains like DFIR or threat hunting. Also, these skills include executable Python scripts, so before letting Claude Code auto-run anything, I should review the `scripts/` folder in security-focused skills, especially red-team and malware-analysis playbooks—standard practice for third-party repos, but more critical here. I'm considering whether to clone the repo and pull the actual skill list by domain so you can hand-pick exactly what to install. The closing offer to clone and list skills by domain is genuinely useful for executing Route 3 and follows naturally from the walkthrough, rather than just rehashing what they already asked for. I'll keep it as the single closing action.Alright. This repo actually loads into Claude Code two different ways — it ships a `.claude-plugin/` directory (so it can install as a native plugin) *and* it's just plain skill folders under `skills/` (so you can drop them in by hand). That gives you three routes, from "everything, fast" to "only what I want, reviewed." I'd point you at the last one — reasons after.

**How Claude Code finds skills** (true regardless of route)

Skills live in one of two spots, each skill as its own folder containing a `SKILL.md`:

- `~/.claude/skills/<name>/` — personal, available in every project
- `.claude/skills/<name>/` — project-scoped, lives in the repo, shareable via git

Claude only reads the YAML frontmatter (name + description, ~30 tokens each) until a skill is actually relevant, then loads the full body. `/skills` in a session lists what's loaded. Editing skills inside an *existing* skills dir hot-reloads mid-session; creating a brand-new top-level skills dir needs a Claude Code restart before it's picked up.

**Route 1 — one-liner, installs all 754**
```
npx skills add mukul975/Anthropic-Cybersecurity-Skills
```
The repo's own installer (agentskills.io CLI). Dumps everything into your skills dir. Fast, but see the 754 caveat below.

**Route 2 — native plugin.** Since it carries `.claude-plugin/`, from inside a Claude Code session:
```
/plugin marketplace add mukul975/Anthropic-Cybersecurity-Skills
/plugin            # Discover tab → install, choose User or Project scope
/reload-plugins    # or restart
/skills            # verify
```
Managed, and easy to pull later (`/plugin` → Installed tab). The exact install name depends on their marketplace manifest — the `/plugin` browser will surface it.

**Route 3 — clone and cherry-pick** (what I'd actually do)
```
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
# copy only the skills you want:
cp -r Anthropic-Cybersecurity-Skills/skills/hunting-for-credential-dumping-lsass ~/.claude/skills/
cp -r Anthropic-Cybersecurity-Skills/skills/analyzing-network-traffic-of-malware ~/.claude/skills/
```
Restart Claude Code, `/skills` to confirm.

**Two things worth knowing before you commit**

*754 is a lot.* Even at ~30 tokens/frontmatter, that's 20k+ tokens of skill metadata competing for attention on *every* task, plus a wall of security skills bleeding into unrelated projects if you install to `~/.claude/`. Unless you want a dedicated security agent, either project-scope it (`.claude/skills/` in a security repo) or cherry-pick the domains you use — DFIR, threat hunting, whatever. That's the real argument for Route 3.

*The skills carry runnable scripts.* Each skill folder has a `scripts/process.py`, and the repo is 99.6% Python. When a skill fires, Claude Code can execute those. Benign for most domains, but this library includes red-team / pentest / malware-analysis playbooks — so skim the `scripts/` of anything you install before letting the agent auto-run it, and keep Claude Code's permission prompts on rather than running with `--dangerously-skip-permissions`. Standard hygiene for any third-party skill repo, more so for a security one off a stranger's GitHub.

Want me to clone it into my sandbox and pull the actual skill list broken out by domain? Then you can pick exact folder names for Route 3 instead of guessing.

---

## 🧑 Papi  <sub>2026-07-04 08:29:54</sub>

just throw something together for me i need to start this project asap

---

## 🤖 Claude  <sub>2026-07-04 08:34:57</sub>

The user wants something concrete to get started on the cybersecurity skills repo integration with Claude Code rather than more discussion. They're asking me to produce actual work output now. I'm weighing whether to just hand them a shell script with a project scaffold versus actually cloning the repo first to get the real skill inventory and folder structure. The script approach is faster and matches what they're asking for, but pulling the actual repo would let me give them accurate skill names and a more thoughtful starter set focused on defensive work like DFIR and threat hunting rather than offensive tools. I'm going to do a shallow clone of the repo to inspect its actual structure without downloading all 754 skills, then build a setup script grounded in what I find rather than assumptions. Once I see the real folder organization, skill naming patterns, and plugin configuration, I can create a genuinely working scaffold they can run immediately.On it. But a setup script built on guessed folder names would just break on you — let me clone the repo and read the *real* structure first, then hand you something that actually runs.
```
This block is not supported on your current device yet.
```

I've cloned the repository and it's about 59 megabytes, so now I'm looking at the top-level directory structure to understand the project layout.
```
This block is not supported on your current device yet.
```

The skills directory has around 817 folders in a flat structure, which is more than the 754 mentioned in the README—possibly due to growth or non-skill directories mixed in. I can see there are both `.claude-plugin/marketplace.json` and `plugin.json` files, indicating this is a proper Claude Code marketplace plugin, so I'll need to check those files to get the correct marketplace and plugin names for the install command. There's also an `index.json` file at 185KB that likely contains a manifest with metadata for all the skills.

I also notice there are `domains` referenced in the index structure, which should help me organize skills by category. There's a `mappings/` directory for framework mappings like ATT&CK and NIST, and a `tools/` directory for shared utilities. My next step is to read the plugin configuration files, examine a sample skill folder to understand the structure, and look at the `index.json` to see how I can curate skills by domain.
```
This block is not supported on your current device yet.
```

I've got the actual marketplace and plugin details now—the marketplace is `anthropic-cybersecurity-skills` and the plugin is `cybersecurity-skills`, so the installation commands would be adding the marketplace first then installing the plugin from it. The skills collection has grown to 817 items organized flat under the `skills/` directory.

Each skill follows a consistent structure with a `SKILL.md` file, reference documentation, an `agent.py` script (not `process.py`), and a license. The folder names use kebab-case and describe the skill—some are clearly offensive like "abusing-dpapi-for-credential-access" and "analyzing-active-directory-acl-abuse," which confirms this is a mixed red-team and defensive library.

I need to check what's actually in those `agent.py` scripts and look at the `index.json` structure to understand how skills are categorized, so I can build an honest assessment of what's runnable and curate a defensive-focused starter set with real skill names.
```
This block is not supported on your current device yet.
```

I can organize the skills by their domain categories and build out a focused defensive toolkit from there.
```
This block is not supported on your current device yet.
```

The `domain` field in index.json is uniformly "cybersecurity" so it won't help with categorization — I'll need to build that myself using keyword matching against the skill names and descriptions. The folder names are already descriptive verb phrases, so I can use those as a basis for creating a curated defensive starter set. Let me examine a sample `agent.py` and `SKILL.md` file to get a sense of the actual content before writing the README.

I'm thinking about what should go into the starter set: incident response, threat hunting, log and SIEM analysis, forensics across disk/memory/network, malware analysis, detection engineering, cloud security posture, vulnerability management, and hardening. I'll deliberately exclude the offensive skills like the "abusing-*" and "exploiting-*" folders from the default — those are available in the repo for users who want them, but a sensible starting point should lean blue-team and practitioner-focused, which is both more broadly useful and the responsible default.

Writing a Python script to bucket the skill folders by keyword and extract the real folder names that match these categories...
```
This block is not supported on your current device yet.
```

So the SKILL.md files actually contain a subdomain field for proper categorization—like "digital-forensics"—which the index.json didn't expose, and the agent.py files are legitimate, functional Python scripts ranging from 150-260 lines, with the forensics one doing real parsing work and the offensive ones appearing to do similar substantive tasks.

I'll write a Python script to parse the YAML frontmatter from all 817 SKILL.md files, extract the name, subdomain, and description, then group them by subdomain so I can select a sensible blue-team starter set.
```
This block is not supported on your current device yet.
```

I'm narrowing down to a practical starter set of defensive security domains for a blue-team agent—incident response, threat hunting, digital forensics, SOC operations, malware analysis, network security, cloud security, vulnerability management, endpoint security, and phishing—picking the highest-impact foundational areas that would deliver immediate value.

Now I'm going to write a script that pulls real skill folder names from each target subdomain and filters for defensively-oriented verbs like analyzing, detecting, investigating, hunting, responding, hardening, and monitoring, then generates a curated list of about 20-25 skills I can review and bake into the setup script.
```
This block is not supported on your current device yet.
```

I've got a solid set of defensive security domains now—real folder names covering 12 practical blue-team areas. Now I'm moving to the actual deliverable and building a runnable project scaffold, starting with a setup script that clones the repo to a temp location and creates the skills directory structure in the current working directory.

I'm also planning a `CLAUDE.md` file to prime Claude Code as a security-focused agent with safety guardrails, and a `README.md` for quickstart instructions. The UX should be straightforward: users save the three files, run the setup script, and they're ready to go with the curated starter set of ~30 defensive skills already in place.

For flexibility, I'm thinking the setup script should support both a default curated mode and optional flags to install specific domains or everything, keeping it simple but extensible. I'm checking whether any of the available skills actually apply here — `skill-creator` is for authoring new SKILL.md files, not for scaffolding a project that uses existing skills, and the other options like frontend-design or the various plugin skills don't fit either. Since I've already consulted product-self-knowledge for the Claude Code context, I can move forward with writing the setup script and markdown config files directly to the outputs folder.

Writing setup script... Writing shell script... Writing shell script logic... Writing documentation files... The scripts contain real, runnable Python code for defensive security tasks, though some domains cover offensive techniques, so I should review any agent-generated scripts before execution and keep permission prompts enabled. I'm thinking through whether to actually test the setup script in my sandbox to verify the folder structure and logic work correctly—I could do a quick dry-run using the existing cloned repo to avoid re-downloading the 59MB archive. That's 27 total across all categories, which matches my estimate. Now I'll write the three files to outputs and run a functional test by seeding the cache from the existing clone and executing the setup script to verify it installs the skills correctly.Repo's real: 817 skills (flat under `skills/`), each with a `SKILL.md` + `references/` + a genuinely runnable `scripts/agent.py` (~150–260 lines each — the offensive ones are real tooling, so my earlier warning holds). It ships a proper `marketplace.json`, and skills self-tag by `subdomain`. I pulled the actual folder names and built you a scaffold around a curated defensive set. Let me write it and test that it runs.
```
This block is not supported on your current device yet.
```

I'll run a syntax check first, then do a functional test by seeding the cache from the existing clone to skip the download step.
```
This block is not supported on your current device yet.
```

The installation script is working correctly—all 27 skills are installing with their complete file structures intact, and the `--list` flag properly displays the subdomain counts. Now I should verify that the `--domain` filtering option works as expected too.
```
This block is not supported on your current device yet.
```

The domain installation worked correctly, bringing the total skill count to 50. Now I'm writing the documentation files—CLAUDE.md and README.md—to output before presenting all three files together.Works end to end — starter set installs 27 skills intact, `--list` and `--domain` both work against the real repo. Now the two project files.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

I'll keep the summary tight and match their casual tone—just the essential steps to get running, with a note about the skills folder being auto-created.Done — three files, tested against the live repo:

Drop all three into a fresh project folder, then:
```bash
bash setup.sh     # pulls 27 curated defensive skills into .claude/skills/
claude            # open Claude Code there → /skills to confirm
```

`setup.sh` also does `--list` (all ~45 subdomains + counts), `--domain <name>` (grab a whole domain like `threat-hunting` or `digital-forensics`), and `--all` (the full 817, if you really want it). It clones once into `.cache/` and reuses it, so adding domains later is instant. `CLAUDE.md` primes the agent as a defensive/DFIR assistant and bakes in the guardrails (authorization, don't blind-run the `agent.py` scripts, keep malware contained). README has the rest.

Starter set is deliberately blue-team — forensics, log/SIEM triage, threat hunting, malware *analysis*, cloud audit, IR, vuln triage. The repo's offensive domains (red-team, pentest, credential-access) are one `--domain` away if you need them for authorized work, but I left them out of the default on purpose.

One thing I want to be straight about, since you're moving fast: I still don't actually know what "this project" is for you. I built the thing this whole thread was pointing at — a working security-skills setup for Claude Code. If you meant something else, tell me and I'll redirect.