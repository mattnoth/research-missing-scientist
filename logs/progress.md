# Session Progress

Every agent session appends here — research, website, tooling, whatever. This is the single durable record of what happened across sessions. The research log (`research-log.md`) tracks research-specific detail; this file tracks everything at session level.

## 2026-04-21 — Mobile timeline + abbreviation tooltips

**What changed:**
- `mattnoth-dev`: Replaced native browser `<abbr title>` tooltips with custom CSS tooltips (`data-tooltip` + `::after`). Accent-colored underline, no more question-mark cursor.
- `mattnoth-dev`: Added mobile-responsive timeline — single-column layout for screens < 600px, left-aligned axis, full-width cards, touch tap-to-reveal tooltips.
- Files: `build/missing-scientists.ts`, `src/styles/missing-scientists.css`, `src/ts/modules/ms-timeline.ts`
- Committed and pushed as `42d3ea7` on mattnoth-dev main.

**Further work:**
- Mobile diagram view still needs attention (deferred — harder problem).
- Should visually test the timeline on actual mobile devices / browser devtools to confirm touch interactions work as expected.
- The abbreviation tooltip `white-space: nowrap` may clip long expansions on narrow screens — monitor and adjust if needed.
