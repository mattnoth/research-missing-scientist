# Prompt Deep-001 — Public Records & Primary Source Deep Dive

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` — print mode. There is no stdin. Make decisions autonomously per the spec. Log ambiguities in `logs/research-log.md` and proceed.

You are Claude Code operating in `/Users/mnoth/source/research-missing-scientists/`. The research repo is populated with 11 case files, analysis, and appendices from prior prompt runs. This prompt deepens the primary-source layer — the current evidence base is ~70% Tier 2 (news media). Your job is to find Tier 1 sources that news outlets referenced but that the original research did not directly locate.

## Hard Safety Rules

- Working directory: `/Users/mnoth/source/research-missing-scientists/`. Do not touch anything outside it.
- No sudo. No system-wide installs.
- No git push. No auth to any service.
- No contacting anyone. Research uses already-public material only.
- Copyright discipline: paraphrase, ≤15 words per quote, one quote per source max.
- If unsure, stop and log the uncertainty.

## Alignment (read `prompts/research/README.md` § "Alignment rules" before starting)

This prompt updates `cases/{slug}.md` files and `appendices/primary-sources/` only. It does not touch analysis files, data files, or the dossier. All changes follow the schema and source discipline established by `prompts/build/prompt-001.md`.

## Strategy

News articles frequently reference primary documents they paraphrased but didn't link. For each case, the sub-agent's job is to trace backward from reported claims to their original sources.

### Source types to hunt (ordered by priority)

1. **Law enforcement records**: Missing persons bulletins (NamUs, state DPS, Silver/Gold Alerts), police press releases, incident reports (public portions), search warrant affidavits (if unsealed)
2. **Court filings**: Criminal complaints, indictments, arraignment records (Grillmair, Loureiro cases especially), probate filings, civil suits
3. **Government records**: FOIA reading rooms (DOE, FBI, NNSA), congressional hearing transcripts and written testimony, GAO reports mentioning relevant programs, Inspector General reports
4. **Institutional records**: Official employer statements, press releases from LANL/JPL/MIT/Caltech/AFRL, organizational charts, annual reports mentioning subjects
5. **Vital records**: Obituaries (official, not news-reported), Find a Grave entries, death index records (where public)
6. **Regulatory filings**: FAA incident reports (if any aircraft involved), OSHA reports, EPA site records for relevant facilities
7. **Congressional records**: House Oversight Committee press releases, hearing schedules, member statements on .gov domains, CRS reports on the topic

### What to do with 403s and dead ends

Prior runs encountered HTTP 403 on several critical URLs. For each:
- Try alternative URL patterns (archived versions, different paths on same domain)
- Search web archives (Wayback Machine / archive.org)
- Search for the document title as quoted in news articles
- If still inaccessible, log in `logs/known-unknowns.md` with the date, URL, and what was tried

## Sub-agent orchestration

Spawn one sub-agent per case (11 total, in parallel). Each sub-agent receives:

### Sub-agent brief (template — fill {slug}, {name}, {case_summary})

```
You are researching primary sources for the {name} case.

Read `cases/{slug}.md` first to understand what sources already exist and what gaps are noted.
Read `appendices/primary-sources/{slug}/` for existing primary source excerpts.
Read `logs/known-unknowns.md` for previously identified gaps in this case.

Your task: find Tier 1 (primary) sources that the existing research references but did not directly obtain. Use web search and web fetch only.

Source types to prioritize:
1. Law enforcement records (missing person bulletins, press releases, incident reports)
2. Court filings (complaints, indictments, arraignment records)
3. Government records (FOIA reading rooms, congressional testimony, IG reports)
4. Institutional records (employer statements, press releases)
5. Vital records (obituaries, Find a Grave, death indexes)
6. Congressional records (Oversight Committee releases, hearing transcripts)

For each source found:
- Verify it is genuinely Tier 1 (primary document, not news reporting about a document)
- Create or update the excerpt file in `appendices/primary-sources/{slug}/`
- Note the source URL, access date, publisher, document type, and date
- Paraphrase; do not reproduce more than 15 words verbatim

For each source NOT found:
- Log what you searched and why it failed in `logs/research-log.md`
- Add or update entry in `logs/known-unknowns.md`

Update `cases/{slug}.md`:
- Add new Tier 1 sources to the Primary Sources section
- If a new source confirms, contradicts, or adds nuance to an existing claim, update the narrative with the new confidence level
- If a new source contradicts an existing claim, add to `logs/contradictions.md`

Do NOT touch: analysis files, data files, dossier.md, other case files.
Do NOT contact anyone. Do NOT invent sources.

Commit your changes with message: `research-deep-001: {slug} primary source expansion`
```

### Orchestrator responsibilities

After all sub-agents complete:

1. Read `logs/research-log.md` to see what each agent found and missed.
2. Read `logs/known-unknowns.md` to see the updated gap list.
3. Write a summary section in `logs/research-log.md`:
   - Date: {today}
   - Prompt: deep-001
   - Cases processed: list all 11
   - New Tier 1 sources found: count and list
   - Sources still missing: count and list
   - 403 URLs retried: results
4. Commit: `research-deep-001: orchestrator summary`

## End conditions

- All 11 cases have been processed by sub-agents.
- `appendices/primary-sources/` updated with any newly found documents.
- `cases/{slug}.md` files updated with new sources (if any).
- `logs/research-log.md` has entries for every search attempt.
- `logs/known-unknowns.md` updated (items resolved or new items added).
- No analysis, data, or dossier files modified.

End of prompt deep-001.
