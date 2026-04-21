# Prompt Alterations

Changes made to downstream prompts by earlier prompts, with rationale.

<!-- Format:
## [prompt filename]
- **Date:** YYYY-MM-DD
- **What was changed:** [description]
- **Why:** [rationale]
-->

## prompt-004.md
- **Date:** 2026-04-21
- **Changed by:** prompt-003
- **What was changed:** Updated Step 6 (downstream regeneration) to clarify that website updates require `npm run build` in mattnoth-dev, not re-running prompt-003.
- **Why:** Prompt-003 is the initial creation prompt — it creates feature branches, installs dependencies, and builds templates from scratch. Re-running it for content updates would fail (branch already exists) or create duplicate work. The website's build system reads the research repo on every build, so a simple `npm run build` picks up all changes.
