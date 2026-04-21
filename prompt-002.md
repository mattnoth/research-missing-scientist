# Prompt 002 — PDF Generation

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` — print mode. There is no stdin. Any question you emit will not be answered and the process will exit. Make decisions autonomously per the spec. If genuinely ambiguous and uncovered by the spec, use best judgment, log in `logs/research-log.md`, and proceed. The only reason to exit non-zero is a hard-safety-rule violation you cannot avoid.

You are Claude Code operating in `/Users/mnoth/source/research-missing-scientists/`. The research repo has been populated by prompt 001. Your job is to produce print-ready PDFs for sharing with people who won't visit the website.

## Hard Safety Rules (unchanged)

- **Working directory only.** Do not touch anything outside `/Users/mnoth/source/research-missing-scientists/`.
- **No system-wide installs. No `sudo`.** `brew install pandoc` is acceptable if pandoc is not already installed — but **ask the user first** and only proceed with explicit approval. Pandoc is widely used, reputable, and widely vetted. Do not install anything else without asking.
- **No git push. No authentication to any service.**
- **No contacting anyone.**
- **If unsure, stop and ask.**

## Downstream prompt alteration

If, in the course of completing this prompt, you identify issues with `prompt-003.md` or `prompt-004.md` that would prevent them from executing correctly — missing context, incorrect assumptions about the PDF outputs or repo state this prompt produces — you may alter them. Document every alteration in `logs/prompt-alterations.md` with: prompt filename, what was changed, why, and the date. Do not alter prompts for stylistic preference; only for correctness.

## Tool requirements

PDF generation needs pandoc and a LaTeX distribution (for pandoc's default PDF engine) OR pandoc with `--pdf-engine=weasyprint` (which uses HTML/CSS, often cleaner for markdown-driven docs). Check what's available first:
- `which pandoc` — check if pandoc is installed
- `which weasyprint` — check if weasyprint is installed
- `which xelatex` — check if LaTeX is installed

If nothing is present: ask the user which engine to install. Recommendation: weasyprint via `brew install weasyprint` is lighter-weight than a full LaTeX distribution, and the HTML/CSS path gives better typographic control for this kind of document. Do not install without asking.

Alternative: if the user already has Node tooling present and prefers, `md-to-pdf` or `markdown-pdf` via `npm` (local to this repo, not global — `npm init -y && npm install --save-dev md-to-pdf`) is also acceptable. Ask.

## Tasks

### 1. Check the repo state
- Confirm all artifacts from prompt 001 exist (check for `STATUS.md`, `dossier.md`, `cases/`, `analysis/`, `appendices/`).
- If `STATUS.md` indicates unresolved issues, surface them to the user and ask whether to proceed.

### 2. Create a PDF styling configuration
- Create a `pdf-config/` directory.
- Write a CSS file (`pdf-config/print.css`) with print-appropriate styling: readable serif body font, clean sans-serif headings, generous margins, page breaks before major sections, footnote-style source tier/confidence indicators, print-friendly colors (high contrast, no reliance on color alone for tier/rating distinctions — use symbols or text labels too).
- Write a pandoc metadata file (`pdf-config/metadata.yaml`) with document title, author ("Matt Noth"), date, and print defaults.

### 3. Generate the main dossier PDF
- Input: `dossier.md` plus all referenced content (case files, analysis, etc.) — either concatenated into a master markdown or rendered as a multi-file document with a table of contents.
- Output: `pdf-output/missing-scientists-dossier.pdf`
- Include a cover page with title, date, abstract, and a clear notice: "Living document — see CHANGELOG.md for version history. Research repository at [local path]. This is not a publication or journalism product; it is a personal research compilation. Sources are categorized by tier, claims by confidence rating."
- Include a table of contents.
- Include the abstract at the top.
- Follow the executive summary.
- Include all case files in case-index order.
- Include analysis files.
- Include appendix content (primary source excerpts, named expert commentary, foreign coverage).
- Include logs (research log, contradictions, known unknowns) as trailing appendices — these demonstrate methodology transparency.

### 4. Generate individual case PDFs
- For each case file in `cases/`, generate `pdf-output/cases/{slug}.pdf`.
- Include per-case header: case name, status, date of PDF generation.
- Include the case's own primary-source appendix entries as an in-PDF appendix.
- Useful when the user wants to send a single case to someone without the full dossier.

### 5. Generate diagram-layer PDFs (three separate files)
Since PDFs cannot do interactive layer toggles, produce one PDF per diagram layer, each rendered from `data/diagram-data.json`:
- `pdf-output/diagrams/connection-diagram-tight.pdf` — tight layer only
- `pdf-output/diagrams/connection-diagram-medium.pdf` — tight + medium
- `pdf-output/diagrams/connection-diagram-corkboard.pdf` — all three layers including corkboard

For rendering, use a simple static approach: either generate SVG from the JSON via a small local script (vanilla JS or Python — do not install anything new if the user has Python 3 already, which is standard on macOS), then convert SVG → PDF via pandoc/weasyprint, or use an existing CLI tool the user already has. If you need to install something, ask.

Every diagram PDF includes a prominent key/legend explaining: node types, edge types, confidence ratings, layer semantics.

### 6. Generate timeline PDF
- `pdf-output/timeline.pdf` — rendered from `data/timeline-data.json`.
- Readable chronological format. Probably wants to be landscape-orientation depending on event density.
- Include a key explaining event types and confidence ratings.

### 7. Update `CHANGELOG.md` and `.gitignore`
- Add an entry to CHANGELOG: `v0.1.1 — PDFs generated`. Dated. Describes outputs.
- Confirm `pdf-output/` is listed in `.gitignore` (if not, add it — PDFs are regeneratable and don't need to be in git; the markdown is the source of truth).

### 8. Final sanity check
- Verify every PDF is non-empty and opens.
- Produce a `pdf-output/README.md` listing every PDF file, its purpose, and its input source (which markdown/JSON drives it).

### 9. Commit
- Commit PDF config, updated `.gitignore`, updated `CHANGELOG.md`.
- Commit message: `build: generate PDFs (dossier, cases, diagrams, timeline)`.
- Do not commit the PDFs themselves (gitignored).
- Do not push.

### 10. Report back
Print:
- List of generated PDFs with sizes
- Any issues encountered
- One-line confirmation that prompt 003 can now begin

## End conditions
Prompt complete when:
- All PDFs generated successfully
- Each PDF has been visually sanity-checked (pandoc didn't produce a zero-byte file or catastrophic layout)
- CHANGELOG updated
- Commit made
- `pdf-output/README.md` exists

Do not touch `mattnoth-dev/`. Do not begin website work. End of prompt 002.
