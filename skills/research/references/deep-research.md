# Deep Research Procedure

Use for multi-question, high-stakes, or contested topics, or when the user asks for a report. Built-in tools only (web search/fetch, file reads, subagents). Paid APIs, MCP search services, or metered data sources only with the user's explicit approval, including a spend limit.

## 0. Frame (lead agent, never delegated)
1. Restate the question and the decision it serves. Check the premise: is the question built on a wrong assumption? Is there an obvious-but-wrong standard answer?
2. Split it into the fewest decision questions that cover the conclusion. For each: why it matters and a stop rule (supported / contradicted / still unknown after named routes).
3. Write 2–3 falsifiable hypotheses, at least one counterintuitive, each with what would overturn it.
4. Set scope: time range, geography, versions, exclusions, and the "as of" date.

## 1. Reuse before searching
Read `research.md` and any notes file for this topic (`references/evidence-notes.md`). Reuse entries still within their review-by date; re-verify stale or version-sensitive ones. Resume an `in-progress` notes file from its "Next steps".

## 2. Plan evidence routes
For each load-bearing claim, name the source owner that can directly observe it (regulator, standards body, maintainer docs and changelog, source code, filing, peer-reviewed study, the vendor's own pricing page). Write 2–3 query variants per question, including synonyms and disambiguating terms.

## 3. Gather (primary first)
- Open and read the 3–5 most important originals closely before any breadth search. Extract claims, data, internal contradictions, what is left unsaid, and the author's incentives.
- Then fill gaps and add breadth. Record sources and claims in the notes file as you go.
- Parallel subagents (optional): at most 3 at a time; each gets the frame, its questions, and the hypotheses; each must return an evidence packet (sources with URLs, excerpts, claim table, counter-evidence) to the lead agent, not files; subagents must not spawn further agents.

## 4. Counter-evidence pass
For each provisional conclusion, search specifically for the opposite: criticism, failures, incidents, "problems with", "alternatives to", newer versions that change the answer. Record what was searched even when nothing was found.

## 5. Verify and grade
Apply `references/source-quality-rubric.md` (claim fitness, independence, evidence families) and run Gates 1–2 of `references/quality-gates.md`. Open the original for every load-bearing claim, conflict, exact number/date, and quotation. Collapse copied sources into one evidence family. Unresolvable conflict → `unknown`, with both sides shown.

## 6. Draft
Structure by argument (observation → analysis → judgment → limits), not by topic. Lead with the answer and the decision it implies. Mark every conclusion `confirmed` / `reported` / `inference` / `assumption`. Include "what we don't know" and the strongest evidence-backed alternative interpretation. End with a numbered source list (title, URL, date/version) that matches the citations exactly.

## 7. Final gates and memory
Run Gates 3–5 of `references/quality-gates.md`. Then save durable conclusions to `research.md` (one line each with label, source, review-by), set the notes file `status: done` (or record "Next steps" if stopping early), and add pending items to `tasks.md`.
