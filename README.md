# Claude Engineering Skills

Rules, skills, and a local memory store that make [Claude Code](https://claude.com/claude-code) work more efficiently. With them installed, Claude reads only the files a task needs, uses only the skill that matches the task, remembers project decisions and pending work between sessions, and keeps its replies short.

Install once per computer. After that, it works in **every project** on that computer automatically. You don't need to copy anything into your projects.

## What's inside

| File | What it does |
|---|---|
| `CLAUDE.md` | Global rules Claude follows in every project: priority, workflow, skill selection, how to read files, memory, research, safety |
| `skills/web-development` | Websites, frontends, backends, APIs, CMS (+ React/Next.js performance rules from Vercel) |
| `skills/web3-development` | Smart contracts, Solidity, dApps, Hardhat/Foundry, OpenZeppelin, Chainlink |
| `skills/automation-bots` | Scrapers, bots, browser automation, scheduled jobs, email/SMS/messaging |
| `skills/debugging` | Finding and fixing the cause of errors |
| `skills/testing` | Writing and running tests |
| `skills/security` | Security reviews, vulnerability fixes, secrets, login/permissions |
| `skills/ui-ux-design` | UX decisions for web, Android, iPhone (flows, states, forms, accessibility, platform rules) |
| `skills/frontend-design` | Distinctive, non-generic visual design (Anthropic, Apache-2.0) |
| `skills/visual-direction` | Which sections need images, what kind, art direction, image delivery |
| `skills/motion` | CSS/JS animation, scroll effects, reduced motion; official GSAP references |
| `skills/threejs-3d` | Three.js, React Three Fiber, WebGL, 3D assets and performance |
| `skills/seo-content` | SEO structure, metadata, schema, local/international SEO, factual copy |
| `skills/prompt-engineering` | Writing and improving prompts without changing intent |
| `skills/research` | Source-checked research saved to memory |
| `docs/third-party.md` | Source, license, pinned commit, and changes for every copied file |
| `memory/` | Local memory store: format rules (`README.md`) and templates. Your entries stay on your computer (gitignored) |
| `scripts/validate.py` | Checks skills, `CLAUDE.md`, and memory for format errors, duplicates, stale entries, and leaked secrets. Python only, no network |
| `docs/maintenance.md` | Architecture, skill-writing standard, checklist for vetting third-party skills |

A skill loads only when your task matches it, so unused skills cost nothing.

---

## Before you start

You need:
1. **Claude Code**, installed and signed in. Check by running `claude --version` in a terminal.
2. **Git**. Check with `git --version`. If it's missing, download it from https://git-scm.com.

> **Already have your own `~/.claude/CLAUDE.md`?** Step 3 below replaces that file and saves the old one as `CLAUDE.md.bak`; add your own rules back into this repo's `CLAUDE.md` (anywhere above the line `## This repo`).

---

## Install on Windows

Open **PowerShell**: press the Start button, type `PowerShell`, and press Enter.

**Step 1: Download the repo.** Pick a folder to keep it in. This example uses `D:\Desktop\Important files`:

```powershell
cd "D:\Desktop\Important files"
git clone https://github.com/ShamratX/claude-engineering-skills.git
cd claude-engineering-skills
```

**Step 2: Install the skills.**

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force skills\* "$HOME\.claude\skills\"
```

**Step 3: Install the global rules and connect the memory store.** Run this inside the repo folder. It writes the memory folder's location into the installed rules.

```powershell
if (Test-Path "$HOME\.claude\CLAUDE.md") { Copy-Item "$HOME\.claude\CLAUDE.md" "$HOME\.claude\CLAUDE.md.bak" }
$mem = (Resolve-Path memory).Path -replace '\\','/'
$lines = Get-Content -Encoding utf8 CLAUDE.md
$end = [array]::IndexOf($lines, '## This repo')
$lines[0..($end-1)] -replace '\{\{MEMORY_ROOT\}\}', $mem | Set-Content -Encoding utf8 "$HOME\.claude\CLAUDE.md"
```

**Step 4:** Close Claude Code and open it again. Done.

> Prefer Git Bash? Use the Mac/Linux commands below instead. Put paths that contain spaces in quotes, for example `cd "/d/Desktop/Important files"`.

---

## Install on Mac or Linux

Open **Terminal**. On a Mac, press Cmd + Space, type `Terminal`, and press Enter.

**Step 1: Download the repo.**

```bash
cd ~
git clone https://github.com/ShamratX/claude-engineering-skills.git
cd claude-engineering-skills
```

**Step 2: Install the skills.**

```bash
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

**Step 3: Install the global rules.**

```bash
[ -f ~/.claude/CLAUDE.md ] && cp ~/.claude/CLAUDE.md ~/.claude/CLAUDE.md.bak
sed -e '/^## This repo/,$d' -e "s|{{MEMORY_ROOT}}|$(pwd)/memory|" CLAUDE.md > ~/.claude/CLAUDE.md
```

**Step 4:** Close Claude Code and open it again. Done.

---

## Check that it worked

1. Open Claude Code in any project and ask: *"Which skills do you have?"* It should list the skills in `skills/`.
2. In Claude Code, type `/memory`. The list should include your user memory file (`~/.claude/CLAUDE.md`).
3. In the repo folder, run `python scripts/validate.py --installed`. It should end with `0 errors`.

---

## Updating after you change something

The installed copies **don't update themselves**. After you edit this repo, or pull changes from GitHub:

1. Open a terminal in the repo folder (`cd` into it).
2. Optional: run `git pull` to get the latest version from GitHub.
3. Run **Steps 2 and 3** again for your system. Skip Step 1 (the repo is already downloaded).
4. Restart Claude Code.

If you **delete or rename** a skill here, also delete its old folder from `~/.claude/skills/`. Copying adds and overwrites files, but never removes them.

---

## Memory

Claude keeps compact notes per project in `memory/`: what the project is, decisions and why, pending tasks, known issues, and short session summaries. It never stores full conversations or secrets.

- Each new session, Claude reads only `memory/INDEX.md` and the two core files of the project you're working in. Other notes are searched, not loaded.
- Claude adds a project the first time it does real work there. You can also edit any file by hand; it's plain Markdown.
- Rules and file format: `memory/README.md`.
- Writing to `memory/` from another project folder may ask for permission. Approve it, or allow that folder in your Claude Code permission settings.
- This repo is public, so your memory entries are **gitignored** and stay on this computer. Back up the `memory/` folder yourself, or make the repo private and remove the `memory/*` lines from `.gitignore` to sync it through git.

---

## Using it on more than one computer

1. On the computer where you made changes: commit and push them (`git add .`, `git commit -m "..."`, `git push`).
2. On the other computer: `git pull` in the repo folder, then Steps 2 and 3 again.

A new computer needs the full install (Steps 1 to 4).

---

## Only for one project (optional)

To give a single project its own copy, for example so teammates get the skills through git, copy the skill folders into that project's `.claude/skills/` folder instead of `~/.claude/skills/`.

---

## Uninstall

- **Skills:** delete this repo's skill folders from `~/.claude/skills/` (on Windows: `C:\Users\<you>\.claude\skills\`).
- **Rules:** delete `~/.claude/CLAUDE.md` (Step 3 saved your previous one as `CLAUDE.md.bak`).
- **Memory:** delete the repo's `memory/` contents except `README.md` and `_template/`.

Restart Claude Code afterwards.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `claude` or `git` is "not recognized" | Install the missing program, then open a **new** terminal. |
| The skills don't show up | Check that each one is at `~/.claude/skills/<name>/SKILL.md`, then restart Claude Code. |
| A path with spaces fails | Put the path in quotes: `cd "D:\Desktop\Important files"`. |
| `sed` is "not recognized" on Windows | You're in PowerShell. Use the Windows commands, not the Mac/Linux ones. |
| Changes don't take effect | Re-run Steps 2 and 3, then restart Claude Code. |

---

## Adding your own skill

Full standard and the checklist for third-party skills: `docs/maintenance.md`.

1. Create `skills/<name>/SKILL.md`. Use a lowercase name with hyphens, like `data-analysis`.
2. Start it with:
   ```markdown
   ---
   name: data-analysis
   description: What it does and when to use it. Also say what it's NOT for.
   ---
   ```
3. Add only rules for that domain, plus a "Not for" boundary. Don't repeat rules that are already in `CLAUDE.md`.
4. Run `python scripts/validate.py`, install it again (Steps 2 and 3), and restart Claude Code.
