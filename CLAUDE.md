# Claude Engineering Skills

A reusable set of engineering skills for Claude Code. Each skill lives in
`skills/<name>/SKILL.md` and holds the conventions, workflow, and checklists
for one kind of work.

## How to use this repo

- **Per project:** copy (or symlink) the skills you need into the project's
  `.claude/skills/` folder.
- **Globally:** copy them into `~/.claude/skills/` so every project can use them.
- Claude loads a skill automatically when the task matches its `description`,
  or you can call it by name (for example `/debugging`).

## Available skills

| Skill | Use it for |
|-------|-----------|
| [web-development](skills/web-development/SKILL.md) | Frontend and backend web apps, APIs, UI work |
| [web3-development](skills/web3-development/SKILL.md) | Smart contracts, Hardhat/Foundry, dApps, wallets |
| [automation-bots](skills/automation-bots/SKILL.md) | Scrapers, Telegram/Discord bots, scheduled jobs, browser automation |
| [debugging](skills/debugging/SKILL.md) | Finding and fixing the root cause of a bug |
| [testing](skills/testing/SKILL.md) | Writing and running unit, integration, and e2e tests |
| [security](skills/security/SKILL.md) | Secure coding, secret handling, reviews before shipping |

## Global working rules

These apply to every task, whichever skill is active.

1. **Read before writing.** Look at the existing code, config, and conventions
   before changing anything. Match the style that is already there.
2. **Small, focused changes.** Change only what the task needs. No drive-by
   refactors unless asked.
3. **Never commit secrets.** Keys, private keys, seed phrases, tokens, and
   `.env` files stay out of git. Use `.env.example` with placeholder values.
4. **Verify your work.** Run the build, the linter, and the tests that cover
   the change. Report failures honestly, with the output.
5. **Ask before irreversible actions.** Deploying to mainnet, deleting data,
   force-pushing, or sending messages to real users needs explicit approval.
6. **Explain the why.** Commit messages and PR descriptions say why the change
   was made, not only what changed.

## Adding a new skill

1. Create `skills/<skill-name>/SKILL.md` (lowercase, hyphenated name).
2. Start the file with frontmatter:

   ```markdown
   ---
   name: skill-name
   description: One or two sentences on what the skill does and when to use it.
   ---
   ```

3. Keep the body practical: workflow steps, conventions, checklists, and
   common mistakes. Put long reference material in extra files next to
   `SKILL.md` and link to them.
4. Add the skill to the table above.
