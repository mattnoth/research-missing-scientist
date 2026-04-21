# Research TODO

Items deferred from the prompt-001 cycle. Revisit before or after PDF/website generation.

## Actionable now (web search could fill)

- [ ] **House Oversight briefing results** — Comer/Burlison requested briefing by April 27, 2026. Check for public statements, press releases, or news coverage of what was disclosed.
- [ ] **FBI investigation updates** — Patel said they'd "produce information to the White House and the world." Search for any findings released since April 20, 2026.
- [ ] **Daily Mail articles** — Original source for Garcia KCNSC employment claim and a key narrative originator for international coverage. Prior searches returned nothing; retry with fresh queries.
- [ ] **BBC coverage** — Absence noted but unconfirmed. One more targeted search to close the gap or confirm the absence.
- [ ] **T1 sources that returned HTTP 403** — BCSO press release PDF, House Oversight press release page. May now be accessible. Retry fetches.

## Formatting fixes (no research needed)

- [ ] **Reza case file** — Add missing section headers: inclusion rationale, named expert commentary, foreign coverage (WION India covered this case).
- [ ] **Hicks case file** — Add inline tier/confidence tags to narrative prose.
- [ ] **Maiwald case file** — Same as Hicks.
- [ ] **Grillmair case file** — Add explicit Documented/Reported/Alleged/Speculated section header (substance already inline).

## Contact list (for future outreach)
- [ ] **Build a people-of-interest list** — Compile names, roles, affiliations, and publicly available contact info for key people across the cases: local beat reporters who covered these stories, named experts quoted in coverage (former FBI, think tank analysts, etc.), family spokespeople who have spoken publicly, congressional staffers involved in oversight hearings. This is prep for eventual direct outreach — no contact until the human operator decides to proceed. Store as a structured file (JSON or markdown table) with name, role, relevance to which case(s), and any public contact info found.
- [ ] **Identify the best local/beat reporters per case** — Who has the deepest coverage? Who broke stories vs. who rewrote wire copy? These are the highest-value outreach targets.

## Re-tag case files for new tier system
- [x] **Update all case file tier references** — Completed 2026-04-21 via `prompts/build/prompt-retag-tiers.md`. All 11 case files migrated.
- [x] **Update dossier.md tier references** — No actionable tier tags found; only Tier 1 references which are unchanged.
- [x] **Update analysis/ tier references** — Already migrated in prior pass; verified correct.
- [x] **Update CLAUDE.md and any prompt files** — Already updated per prompt-retag-tiers.md exclusion list.

## Significant gaps (harder to fill)

- [ ] **Base-rate actuarial analysis** — Compare observed rate (11 events, ~4-year window) against expected rate for the combined defense/aerospace workforce (~30k+ across LANL, JPL, Sandia, KCNSC, etc.). Most important analytical gap. May require workforce demographic data that isn't freely public.
- [ ] **Non-English foreign coverage** — Search TASS, Xinhua, Press TV, NHK, Al Jazeera, Le Monde, Der Spiegel, Haaretz in native languages. Only English-language editions were searched in prompt-001.
- [ ] **Reza-McCasland professional connection** — WION flagged a "Mondaloy connection." Both touched the AFRL ecosystem. No documented link found yet. Patent co-author networks, conference proceedings, or AFRL contract records might surface something.

## Cannot fill with open-source research

- Classified program overlap between subjects (only FBI/DOE/DOD can address)
- Inter-case social network analysis from phone/email records
- Cell phone forensic results for Reza (LASD has not released)
- McCasland USAF sweatshirt forensic results (pending)
- Hicks and Maiwald autopsy status (LA County ME has not confirmed or denied)




- can we get around the above?
- make the prompt resuable in such a way as to update the research. also ask if i can put that on an automatic clock to the deployed website for updated research every day?

## Automated Trigger
- [ ] **Set up a scheduled Claude Code trigger** to run prompt-004 (maintenance/update) on a daily or weekly cron. Should: check for new developments (House Oversight findings, FBI updates, new cases, case resolutions), update research artifacts, bump version, and flag if PDFs/website need regeneration. Needs: a trigger prompt adapted from prompt-004 that runs non-interactively and commits results. Consider whether to also auto-rebuild the website (`npm run build` in mattnoth-dev) or just flag it for manual rebuild.

## Website — Timeline Improvement
- [ ] Better layout and spacing — current visualization is too basic
- [ ] More readable event labels and descriptions
- [ ] Improved zoom/scroll UX
- [ ] Better mobile experience (consider vertical layout for mobile)
- [ ] Group overlapping events more clearly
- [ ] Add more context events (media milestones, congressional actions)

## Website — Diagram Enrichment
The connection diagram needs significantly more data to match the richness of the research:
- [ ] Add more specific locations (Los Alamos neighborhoods, specific trails, specific addresses)
- [ ] Add specific projects/programs (DART, NEAT, Dawn for Hicks; Mondaloy for Reza; PSFC fusion programs for Loureiro; SAPs for McCasland)
- [ ] Expand speculative/corkboard layer — research contains extensive speculation analysis not yet visualized
- [ ] Add behavioral pattern nodes (left without belongings, undisclosed cause of death)
- [ ] Consider temporal proximity edges (events close in time)
- [ ] Current: 34 nodes / 44 edges — research supports significantly more

## Website — Diagram Interactivity & Animations
- [ ] **Fix click-to-highlight connections** — Current implementation isn't working well; clicking a node should reliably highlight its direct connections and dim everything else. Needs debugging.
- [ ] **Make connection lines clickable** — Clicking an edge should show details about the relationship (type, strength, relevant cases, etc.)
- [ ] Make graph nodes clickable (navigate to relevant case or detail)
- [ ] Add more cool animations to the diagram (transitions, hover effects, edge pulses, etc.)

## Website — Diagram Layout & Readability
- [ ] **Fix force-directed auto-spreading** — When there are too many nodes, the graph is unreadable because nodes pile up on top of each other. The auto-spreading/repulsion that should be keeping nodes apart isn't working. Investigate force simulation parameters (charge strength, link distance, collision radius) and fix so the graph scales gracefully as node count grows.

## Website — UFO/UAP Section
- [ ] Create a dedicated page or section focused on UFO/UAP/alien theories and these scientists' connections to that world
- [ ] Make it prominent in the site navigation (not buried)
- [ ] Collect and link evidence tying cases to UAP-related programs, congressional hearings, whistleblower claims, etc.
- [ ] Include outbound links to key UAP sources (congressional testimony, AARO reports, Grusch claims, etc.)

## Website — Diagram Styles
- [ ] Experiment with a traditional corkboard-style diagram (straight lines, pinned cards, string connections) as an additional view alongside the existing force-directed graph
- [ ] Try other diagram layout styles (hierarchical, radial, etc.) to see what communicates the connections best

## Website — SEO Optimization

### Head / Meta Tags
- [ ] Add proper `<title>` tags per page (descriptive, keyword-rich, under 60 chars)
- [ ] Add `<meta name="description">` per page (compelling summary, under 160 chars)
- [ ] Add Open Graph tags (`og:title`, `og:description`, `og:image`, `og:url`) for social sharing
- [ ] Add Twitter Card meta tags (`twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`)
- [ ] Add canonical URLs (`<link rel="canonical">`) to avoid duplicate content issues
- [ ] Add structured data / JSON-LD (Article schema for case pages, WebSite schema for homepage)
- [ ] Ensure proper `<meta name="robots">` directives
- [ ] Add favicon and `apple-touch-icon` if missing

### In-Article Links & Structure
- [x] Add internal cross-links between related case pages (e.g., Reza ↔ McCasland, Hicks ↔ Grillmair) — Completed 2026-04-21. All 11 case files now have "Related Cases" and "Analysis Cross-References" sections. Analysis files have case back-links in all key tables.
- [x] Link from case pages to relevant analysis sections and vice versa — Completed 2026-04-21. Case→analysis links in every case file; analysis→case links in connection-analysis.md, hypotheses.md, and foreign-intel-layer.md.
- [x] Add outbound links to authoritative sources (news articles, government pages, congressional records) — Already present. All case files have source tables with links to LASD, BCSO, House Oversight, USPTO, DOJ, MIT, Caltech, Forest Lawn, and major news outlets.
- [x] Use descriptive anchor text (not "click here" — use "House Oversight hearing on scientist deaths") — Already clean. No generic anchor text found in any file.
- [ ] Add a sitemap.xml and submit to Google Search Console — **Website repo task** (mattnoth-dev), not this research submodule.
- [x] Ensure proper heading hierarchy (single H1 per page, logical H2/H3 nesting) — Verified 2026-04-21. All 25 markdown files pass: single H1, logical H2/H3 nesting, no skipped levels.
- [ ] Add breadcrumb navigation with structured data — **Website repo task** (mattnoth-dev), not this research submodule.

### Keywords & Search Visibility
- [ ] Target high-search terms: "missing scientists", "dead scientists 2024 2025", "Los Alamos deaths", "defense scientist deaths", "scientists disappearing", "UAP scientists killed"
- [ ] Target adjacent buzz topics: "government cover-up scientists", "whistleblower scientists", "AARO", "David Grusch", "congressional UFO hearings", "classified programs scientists"
- [ ] Include long-tail keywords naturally in case narratives: names + affiliations + locations + circumstances
- [ ] Add an FAQ section or page targeting question-based searches ("Why are so many scientists dying?", "What happened to scientists at Los Alamos?")
- [ ] Optimize image alt text with descriptive, keyword-relevant descriptions
- [ ] Consider a blog/updates section for fresh content signals (Google favors regularly updated sites)
- [ ] Monitor Google Trends for emerging related search terms and update content accordingly

## Website — Community Contributions
- [ ] **User-submitted connections on the diagram** — Allow visitors to suggest new nodes/edges (e.g., "I think X is connected to Y because…"). Could be a simple form that creates a GitHub issue or a moderated submission queue. Decide: live on site vs. PR-based workflow.
- [ ] **CONTRIBUTING.md in the research repo** — Document how someone can contribute: how to submit a new case or connection, the source-tiering and confidence-rating requirements, the case file schema, and the no-contact policy. Lower the barrier for open-source researchers.
- [ ] **Contributing guide on the website** — A public-facing "How to Contribute" page (friendlier than a raw markdown file) explaining what kinds of contributions are welcome: new cases, source links, corrections, foreign-language coverage, FOIA documents, etc.
- [ ] **Moderation / review process** — Define how submissions get vetted before merging (source tier check, neutrality review, no doxxing/contact). Could be maintainer-only review or a small trusted-reviewer group.

## Website — Natural Language Research Chat (far future)
- [ ] **Embed a chat interface on the website** — Let visitors ask questions in natural language about the cases, connections, and research (e.g., "Which scientists worked at LANL?", "What are the UAP connections?"). Powered by an LLM with this repo as its knowledge base / RAG context.
- [ ] **Use repo as a research harness** — Allow the chat to kick off new research prompts against the repo's prompt pipeline, returning structured results. Essentially turning the site into an interactive research tool, not just a static dossier.
- [ ] **Scope and safety guardrails** — Enforce the no-contact policy, source-tiering standards, and neutrality rules within the chat. Prevent the model from fabricating claims or presenting speculation as fact.

## Website — UI Polish
- [ ] Change the question mark icon
