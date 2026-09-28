# Claude Engineering Skills

Rules and skills that make [Claude Code](https://claude.com/claude-code) work more efficiently. With them installed, Claude reads only the files a task needs, uses only the skill that matches the task, and keeps its replies short.

Install once per computer. After that, it works in **every project** on that computer automatically. You don't need to copy anything into your projects.

## What's inside

| File | What it does |
|---|---|
| `CLAUDE.md` | Global rules Claude follows in every project: workflow, planning, architecture, how to read files, accuracy, safety |
| `skills/web-development` | Websites, frontends, backends, APIs, CMS |
| `skills/web3-development` | Smart contracts, Solidity, dApps, Hardhat/Foundry, OpenZeppelin, Chainlink |
| `skills/automation-bots` | Scrapers, bots, browser automation, scheduled jobs, email/SMS/messaging |
| `skills/debugging` | Finding and fixing the cause of errors |
| `skills/testing` | Writing and running tests |
| `skills/security` | Security reviews, vulnerability fixes, secrets, login/permissions |

A skill loads only when your task matches it, so unused skills cost nothing.

---

## Before you start

You need:
1. **Claude Code**, installed and signed in. Check by running `claude --version` in a terminal.
2. **Git**. Check with `git --version`. If it's missing, download it from https://git-scm.com.

> **Already have your own `~/.claude/CLAUDE.md`?** Step 3 below replaces that file. Save a copy of it first, then add your own rules back into this repo's `CLAUDE.md` (anywhere above the line `## This repo`).

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

**Step 3: Install the global rules.**

```powershell
$lines = Get-Content CLAUDE.md
$end = [array]::IndexOf($lines, '## This repo')
$lines[0..($end-1)] | Set-Content -Encoding utf8 "$HOME\.claude\CLAUDE.md"
```

**Step 4: Install Caveman,** the tool that shrinks long output to save tokens:

```powershell
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

**Step 5:** Close Claude Code and open it again. Done.

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
sed '/^## This repo/,$d' CLAUDE.md > ~/.claude/CLAUDE.md
```

**Step 4: Install Caveman.**

```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

**Step 5:** Close Claude Code and open it again. Done.

---

## Check that it worked

1. Run `claude plugin list`. You should see `caveman@caveman` with status **enabled**.
2. Open Claude Code in any project and ask: *"Which skills do you have?"* It should list the six skills above.
3. In Claude Code, type `/memory`. The list should include your user memory file (`~/.claude/CLAUDE.md`).

---

## Updating after you change something

The installed copies **don't update themselves**. After you edit this repo, or pull changes from GitHub:

1. Open a terminal in the repo folder (`cd` into it).
2. Optional: run `git pull` to get the latest version from GitHub.
3. Run **Steps 2 and 3** again for your system. Skip Step 1 (the repo is already downloaded) and Step 4 (Caveman is already installed).
4. Restart Claude Code.

To update Caveman itself: `claude plugin update caveman@caveman`, then restart.

If you **delete or rename** a skill here, also delete its old folder from `~/.claude/skills/`. Copying adds and overwrites files, but never removes them.

---

## Using it on more than one computer

1. On the computer where you made changes: commit and push them (`git add .`, `git commit -m "..."`, `git push`).
2. On the other computer: `git pull` in the repo folder, then Steps 2 and 3 again.

A new computer needs the full install (Steps 1 to 5).

---

## Only for one project (optional)

To give a single project its own copy, for example so teammates get the skills through git, copy the skill folders into that project's `.claude/skills/` folder instead of `~/.claude/skills/`.

---

## Uninstall

- **Skills:** delete the six skill folders from `~/.claude/skills/` (on Windows: `C:\Users\<you>\.claude\skills\`).
- **Rules:** delete `~/.claude/CLAUDE.md`.
- **Caveman:** `claude plugin uninstall caveman@caveman`.

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

1. Create `skills/<name>/SKILL.md`. Use a lowercase name with hyphens, like `data-analysis`.
2. Start it with:
   ```markdown
   ---
   name: data-analysis
   description: What it does and when to use it. Also say what it's NOT for.
   ---
   ```
3. Add a `**Caveman**` line (what output to shrink, what to keep in full), then only rules for that domain. Don't repeat rules that are already in `CLAUDE.md`.
4. Install it again (Steps 2 and 3) and restart Claude Code.
