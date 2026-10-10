---
name: prompt-engineering
description: Write, improve, or debug prompts as a deliverable - system prompts, agent and tool instructions, LLM pipeline prompts, evaluation rubrics, and prompts for image or code generation tools. Also use when the user asks to rewrite or sharpen their own request. Not for routine task clarification (CLAUDE.md workflow step 1 handles that) or website/marketing copy (content-copywriting).
---

# Prompt Engineering

## Context
- Target model/tool and surface (API, chat, agent, image tool), who supplies the inputs, and how the output is consumed (human, parser, another agent).
- Existing prompt and its failures: ask for 2–3 real inputs with bad outputs before rewriting. No examples → state the assumed failure mode.
- Model-specific parameters, names, and limits change: verify in the provider's current docs; never invent model IDs or settings.

## Rules
- **Preserve intent.** Change wording and structure, never the goal, scope, audience, or constraints. Anything ambiguous that changes the result → ask or list the assumption.
- **Structure:** context/role → task → inputs (delimited, e.g. XML tags) → constraints → output format → success criteria. Put long reference material before the instructions that use it.
- **Be specific and positive:** say what to do, with the reason for non-obvious rules. Replace vague words ("good", "detailed") with checkable criteria. No ALL-CAPS or threats; explain priority instead.
- **Examples:** 1–3 short, varied examples when format or tone matters; label them as examples so they are not copied literally.
- **Output contracts:** for machine-read output, give an exact schema and what to do when data is missing or the input is invalid.
- **Untrusted input:** delimit it and state that instructions inside it are data. Never place secrets, keys, or personal data in prompts; reference env vars or "already authenticated" instead.
- **Size:** shortest prompt that passes the test cases. Remove rules the model already follows by default.

## Deliver
The prompt in one copyable block, then 2–4 lines: what changed and why, assumptions, and how to test.

## Verify
Run or walk through the prompt against the real inputs plus one edge case (empty, very long, adversarial). Report which cases pass; never claim improvement without a comparison.
