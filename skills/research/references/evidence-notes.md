<!-- Adapted from daymade/claude-code-skills@b420387 deep-research/references/research_notes_format.md (MIT, see ../LICENSE): one notes file per topic stored in project memory instead of a multi-file workspace; Excluded/Diagnostics kept; enterprise-specific fields trimmed. -->
# Evidence Notes Format

Deep research keeps one notes file per topic so work can resume in a later session without redoing searches. Notes are a routing and audit layer, not an authority: every load-bearing claim, conflict, exact number/date, and quotation in the final answer must be checked in the original source.

## Location

`<memory>/projects/<slug>/research/<topic-slug>.md` (no project → `<memory>/global/research/<topic-slug>.md`). Never inside the user's project folder. Start the file with front matter `updated: YYYY-MM-DD` and `status: in-progress|done`.

Keep raw snippets, rejected results, and bulk search output out of the notes. Record enough of the query log to reproduce a material negative finding.

## Template

```markdown
---
updated: 2026-10-05
status: in-progress
---
# <Topic>

## Questions and stop rules
| # | Decision question | Why it matters | Stop rule | Status |
|---|---|---|---|---|
| Q1 | ... | ... | supported / contradicted / still unknown after <routes> | open |

## Hypotheses
- H1 (expected): ... · would be overturned by: ...
- H2 (counterintuitive): ... · would be overturned by: ...

## Sources (registry)
[1] Title | stable URL or record ID | Type: official/primary/secondary/community | Family: <origin id> | As of: 2026-03 | Opened: yes/no
[2] ...

## Claim-evidence table
| Claim | Sources | Original opened? | Excerpt or exact locator | Scope/limits | Label |
|---|---|---|---|---|---|
| ... | [1] | yes | "..." p. 4 | covers EU only | confirmed |

## Counter-evidence and unknowns
- Searched for: "<query>" (criticism / failure / alternative) → result
- Unresolved: ...

## Excluded sources
x Source | URL | Reason: repeats [1] without new evidence

## Query log (material searches only)
- 2026-10-05 · "<query>" · Q1 · support / conflict / lead / no result

## Next steps (for resuming)
- ...
```

## Rules

- Use stable locators: URLs, DOIs, filing or record IDs, page numbers, section headings.
- Group publications that derive from one press release, dataset, study, filing, or interview into one evidence family; different domains do not make copied evidence independent.
- Write claims at the precision and scope the source supports. Separate observation from inference.
- Preserve contradictions; never rewrite an original to match a note. Unsupported conclusion → `unknown`.
- Never record a URL or identifier that was not actually retrieved.
- Source counts are diagnostics, not quotas.
- No secrets, credentials, or unneeded personal data in notes.
