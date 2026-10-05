# Source

- `SKILL.md`, `references/deep-research.md`: in-house.
- `references/source-quality-rubric.md` (unchanged), `references/quality-gates.md` (adapted), `references/evidence-notes.md` (adapted): from https://github.com/daymade/claude-code-skills, path `deep-research/references/` (`source_quality_rubric.md`, `quality_gates.md`, `research_notes_format.md`).
  - Author: daymade. License: MIT (`LICENSE`).
  - Commit: b4203875314da755428e2011292c608876e61810 (these three files last changed upstream in da2b2d05ebdab5599911ec9037e3b6c1c587cfe6, 2026-09-08).
  - Audited: 2026-10-05. The three files read in full; Markdown only, no scripts, hooks, network calls, credentials, or dependencies. Links in the rubric point to public method sources (Cochrane, GAO, SEC, USAspending, GOV.UK).
  - Changes: `quality-gates.md` phase labels P2–P7 renamed to this skill's steps. `evidence-notes.md` rewritten from `research_notes_format.md` to a single notes file per topic stored in project memory (resumable), with enterprise-specific fields trimmed. Each changed file says so in its first line.
  - Not copied: upstream `SKILL.md` (33 KB), `scripts/provider_runs.py` and `scripts/research_assets.py` (mandatory Python run/asset tooling), provider/paid-route contracts, enterprise frameworks, report templates, tests.
  - Reason: strongest source-verification and anti-hallucination method among audited candidates, from an actively maintained repository; vendored as on-demand references so the skill stays small and needs no scripts or paid services.
  - Review by: 2027-01-05.
- Other candidates audited 2026-10-05 and not used: Weizhena/Deep-Research-skills (structured wide research, needs a Python validator, weaker source verification); SeanEllyJames/deep-research-skill (good method, but 3 commits from one day, single maintainer); 199-biotechnologies/claude-deep-research-skill (no LICENSE file, Python and PDF-rendering dependencies); affaan-m/ECC deep-research and research-ops (require paid Firecrawl/Exa MCPs or the ECC stack); K-Dense-AI research-lookup (paid Parallel API key); Imbad0202/academic-research-skills (CC BY-NC 4.0, non-commercial); mvanhorn/last30days-skill (social-trend scraping via third-party APIs); gpt-researcher, open_deep_research, dzhng/deep-research (standalone apps needing API keys, not Claude Code skills).
