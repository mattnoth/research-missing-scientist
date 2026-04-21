# Prompt 003 — Website Integration

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` — print mode. There is no stdin. Any question you emit will not be answered and the process will exit. Make decisions autonomously per the spec. If genuinely ambiguous and uncovered by the spec, use best judgment, log in `logs/research-log.md`, and proceed. The only reason to exit non-zero is a hard-safety-rule violation you cannot avoid.

You are Claude Code. For this prompt only, you may operate in **both**:
- `/Users/mnoth/source/research-missing-scientists/` (read-only — this is the research source of truth)
- `/Users/mnoth/source/mattnoth-dev/` (read/write — this is the user's personal website)

Your task is to build the `/unpublished/missing-scientists` section of the user's website, consuming the research artifacts produced by prompts 001–002.

## Hard Safety Rules

- **Working directories are the two listed above. Nothing else.**
- **Research repo is read-only in this prompt.** Do not modify it. If you notice issues in the research, write them to `/Users/mnoth/source/research-missing-scientists/logs/website-integration-notes.md` (the only write you may make to the research repo) — do **not** silently fix research content while building the website.
- **No system-wide installs. No `sudo`.** `brew` and `npm` are acceptable for reputable packages where warranted, but **ask first** before installing anything.
- **No framework installs.** The user has been explicit: vanilla TypeScript and CSS. D3 via npm is acceptable if genuinely warranted for the interactive diagram — ask first. No React, no Vue, no Svelte, no Next, no Astro. No CSS frameworks (no Tailwind, no Bootstrap). Hand-written CSS.
- **Branch workflow:** create a feature branch (`feature/missing-scientists`) for all website work. Commit there. When everything works end-to-end and you've verified navigation, merge to `main` locally. **Do not push** — the user pushes.
- **No git remote operations. No authentication.**
- **No contacting anyone.**
- **If unsure, stop and ask.**

## Downstream prompt alteration

If, in the course of completing this prompt, you identify issues with `prompt-004.md` that would prevent it from executing correctly — for example, if the maintenance prompt would need to know about website-specific artifacts or conventions you've established here — you may alter it. Document every alteration in `logs/prompt-alterations.md` (in the research repo, since that's the shared state) with: prompt filename, what was changed, why, and the date. Do not alter prompts for stylistic preference; only for correctness.

## Step 1 — Survey the existing website

Before writing any code, read the existing `mattnoth-dev/` repo thoroughly:
- Look for `CLAUDE.md`, `README.md`, `AGENTS.md`, or similar docs describing the project.
- Understand the build system (is it plain `tsc`? esbuild? vite? a custom script?).
- Understand the file structure — where do pages go, where does CSS go, where do shared components go.
- Understand how existing pages handle navigation, headers, footers.
- Identify URL routing — how does a path like `/unpublished/missing-scientists` get served. Is it a static file mapped by the server? A routing layer? Flat-file?
- Note any existing conventions: naming, formatting, accessibility patterns, color scheme, typography.
- Check for an existing `unpublished/` area or routing convention for unpublished content — if one exists, follow it.

If any of this is unclear, **ask the user before writing code.** Don't guess at project conventions.

Document your findings in a scratch file in your working state so you can reference it throughout.

## Step 2 — Plan the site structure

Decide the page structure for `/unpublished/missing-scientists/`. Use your judgment; a reasonable default:
- **Landing page** — abstract, executive summary, navigation to all sub-areas, case index
- **Case pages** — one per case, with the full case-file content and primary-source excerpts
- **Analysis pages** — connection analysis, hypotheses, foreign-intel layer (could be one page or three; your call)
- **Diagram page** — interactive connection diagram with layer toggles (tight/medium/corkboard)
- **Timeline page** — interactive or scroll-through timeline
- **Sources page** — consolidated index of all primary sources, named-expert commentary, foreign coverage
- **Methodology page** — pulls from README methodology section — why this matters for a reader who wants to trust the research
- **Logs page** (optional, transparency-forward) — research log, contradictions, known unknowns. Marks the repo as transparently epistemically honest.

Every page needs:
- Consistent header with breadcrumb navigation
- "Back to index" link
- Next/previous navigation where sequential (cases, for example)
- Footer with last-updated date, link to research repo info, version from CHANGELOG

### Navigability requirements (user explicit)
- People the user sends the link to must be able to navigate easily.
- Clear persistent nav (not just hamburger; should be visible on desktop).
- Table of contents on long pages (case pages, analysis pages, dossier landing).
- Clickable nodes in the diagram must deep-link to the corresponding case page.
- Timeline events must deep-link to the corresponding case page.
- Every page works on mobile.
- Every page works with JavaScript disabled for the text content (JS is required only for the diagram interactivity).

## Step 3 — Build the content pages

Render the research markdown into HTML pages. Use a markdown-to-HTML toolchain the user already has, or install a reputable one after asking — `marked` or `markdown-it` via npm (local to the project) are acceptable. If the user's existing build does something different, match it.

Preserve source tier labels and confidence ratings visibly. These are part of the value — don't hide them. Suggest styling: small superscript-style badges for tier, inline text labels for confidence rating, with a persistent key in the footer or sidebar.

## Step 4 — Build the interactive diagram

This is the centerpiece. Requirements:
- **Consumes `data/diagram-data.json`** from the research repo.
- **Three layers: tight / medium / corkboard.** Default view shows tight layer only. Toggles (visible, obvious) let the user add medium and/or corkboard.
- **Key/legend always visible.** Explains node types, edge types, edge layer styling, confidence ratings.
- **Pan/zoom.** Users can move around the diagram.
- **Clickable nodes** navigate to the corresponding case page (or institution/program info page if nodes represent non-person entities).
- **Hover reveals** the full metadata for nodes and edges — including the evidence pointer (which case file supports this connection).
- **Responsive** to browser size.
- **Accessible** — keyboard navigation to nodes, ARIA labels where appropriate.

Implementation: **vanilla TypeScript with D3.js**, if D3 is acceptable to the user (ask first). D3 is the standard for custom interactive graph visualizations and is worth the dependency. If the user prefers no dependencies at all, use raw SVG + `svg-pan-zoom` (a small standalone library) or hand-roll pan/zoom — warn that development takes longer and iteration is harder. Default recommendation: D3.

Layer styling:
- **Tight layer edges:** solid lines.
- **Medium layer edges:** dashed lines.
- **Corkboard layer edges:** dotted lines, lower opacity.
- **Confidence ratings** indicated on edges by thickness, color, or explicit label on hover (do not rely on color alone).

## Step 5 — Build the interactive timeline

Consumes `data/timeline-data.json`. Requirements:
- Horizontal chronological layout, zoomable/scrollable.
- Events color/icon-coded by type (disappearance / death / investigation milestone / institutional statement / political event).
- Clicking an event navigates to the case page (where applicable).
- Key/legend visible.
- Responsive.
- Accessible — keyboard nav.

Implementation: vanilla or minimal library. D3 can handle this too. `vis-timeline` is an alternative but heavier — prefer hand-rolled or D3 unless there's a reason.

## Step 6 — Styling

Hand-written CSS, following the conventions of the existing website. If the existing site has a typography system, color tokens, spacing scale, use them. If not, establish modest ones in a `missing-scientists.css` file scoped to this section.

Visual register: neutral, academic, not sensational. Readable. Accessible contrast (WCAG AA minimum). Print-friendly CSS via `@media print` for anyone who prints pages directly from the browser.

## Step 7 — Testing

Before merging:
- Build the site locally and navigate every page.
- Click every nav link. Click every diagram node. Click every timeline event. Verify deep links resolve correctly.
- Test mobile breakpoints.
- Test with JavaScript disabled — confirm content still reads.
- Verify the diagram key and timeline key are visible.
- Verify source tier and confidence rating labels are visible throughout.
- Check that no absolute file paths from the user's machine leak into the rendered site.
- Confirm no content from outside the research repo accidentally got included.

Document any issues in a `website-integration-notes.md` at the research repo, then fix them in the website repo.

## Step 8 — Merge and report

When everything works end-to-end:
- Verify you are on the `feature/missing-scientists` branch.
- Final commit on the branch with message: `feat: add /unpublished/missing-scientists page and subpages`.
- Checkout `main`.
- Merge the feature branch: `git merge --no-ff feature/missing-scientists`.
- **Do not push.**
- Report to the user:
  - Local URL to view the page (e.g., `http://localhost:XXXX/unpublished/missing-scientists` or the relevant file path)
  - Summary of pages created
  - Any dependencies added (with versions)
  - Any deviations from original plan
  - Instructions for pushing when ready

## Step 9 — Write the website section's own README

In the website repo at the new section's location, write a small `README.md` (if the project convention allows) describing:
- What this section is
- How it consumes the research repo
- How to rebuild after research updates
- Any scripts added to the project

## End conditions
- Feature branch merged to main locally, unpushed.
- All pages render, all navigation works.
- Diagram and timeline are interactive and correct.
- User has been reported to and knows how to push.

End of prompt 003.
