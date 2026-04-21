# Prompt 004 — Maintenance / Update

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` — print mode. There is no stdin. Any question you emit will not be answered and the process will exit. Make decisions autonomously per the spec. If genuinely ambiguous and uncovered by the spec, use best judgment, log in `logs/research-log.md`, and proceed. The only reason to exit non-zero is a hard-safety-rule violation you cannot avoid.

You are Claude Code operating in `/Users/mnoth/source/research-missing-scientists/`. The research repo exists and has been populated by prompts 001–003 previously. This prompt runs **periodically on demand** (not in the initial chain). Its purpose is to update the living artifact when new information drops.

## Hard Safety Rules (unchanged)

- Working directory: `/Users/mnoth/source/research-missing-scientists/`. May also read (not write) `/Users/mnoth/source/mattnoth-dev/` if needed to confirm website state.
- No system-wide installs. No `sudo`. No unasked package installs.
- No git push. No auth to any service.
- No contacting anyone.
- If unsure, stop and ask.

## Downstream prompt alteration

This is the last prompt in the series, so there are no downstream prompts to alter. However, if in the course of this update you identify that `prompt-004.md` itself — the prompt you are currently executing — has issues or gaps based on what you learned, you may edit it for future runs. Document every self-edit in `logs/prompt-alterations.md` with: what was changed, why, and the date. Do not alter for stylistic preference; only for correctness.

## When to run this prompt
- New case surfaces publicly.
- Existing case resolves (body found, suspect identified, charges filed, person located).
- House Oversight Committee releases findings or holds hearings.
- White House/FBI releases official statements.
- Major new reporting surfaces in a credible outlet.
- A substantial amount of time has passed and you want a full refresh.

The user will typically tell you in their message what triggered the update. If not, ask: "What triggered this update? (new case / case resolution / official findings / major reporting / general refresh)"

## Tasks

### 1. Read the current state
- Read `CHANGELOG.md` to see what's been produced so far.
- Read `STATUS.md` if present.
- Read `logs/known-unknowns.md` to see what was previously unresolvable.
- Ask the user: "Which areas should this update focus on?" Present options: (a) specific case(s), (b) cross-case analysis refresh, (c) new case addition, (d) full refresh, (e) other.

### 2. Scoped research
Based on what the user selected, run targeted research. Use the same source discipline as prompt 001:
- Tiered sourcing
- Confidence ratings per claim
- Copyright discipline
- Refuse-to-invent rule
- No contacting anyone
- Foreign-press coverage where relevant (don't drop countries; also don't add commentary not present in the research)

You can spawn sub-agents for this the same way prompt 001 did, scaled to the scope. For a single-case update, one agent. For a full refresh, full orchestration.

### 3. Update artifacts
For each affected artifact:
- Make the edit with a clear commit.
- Update the case file's "last reviewed" timestamp if your schema supports it.
- Re-check the case's contradictions against new sources — add to `logs/contradictions.md` if new conflicts appeared.
- Update `logs/known-unknowns.md` — remove resolved items with a note, add new unknowns.
- Append to `logs/research-log.md` describing what was searched and found in this update pass.

If the update changes any connection in the diagram or event in the timeline:
- Update `data/diagram-data.json` and `data/timeline-data.json`.
- Flag that PDFs (prompt 002) and website (prompt 003) will need regeneration.

### 4. Update the dossier if warranted
- Abstract and executive summary are rewritten only if findings have changed materially.
- If findings are stable and only a case-level detail changed, the abstract stays.

### 5. Bump the version and CHANGELOG
- Use semantic versioning at the repo level: major changes (new hypothesis, substantial reframing) bump minor version; case-level updates bump patch.
- Add a CHANGELOG entry with date and scope.

### 6. Ask about downstream regeneration
- If content affecting PDFs changed: "PDFs are out of date. Run prompt 002 now to regenerate? (yes/no)"
- If content affecting website changed: "Website is out of date. Run prompt 003 now? (yes/no)"
- Do not run them without explicit user confirmation.

### 7. Commit and report
- Commit with scope-prefixed messages.
- Do not push.
- Report:
  - What was updated
  - What sources were added
  - Any contradictions or known unknowns that changed
  - Whether PDFs/website need regeneration

## Not your job in this prompt
- Do not regenerate PDFs (that's prompt 002).
- Do not touch `mattnoth-dev/` content (that's prompt 003).
- Do not rewrite things that didn't change.
- Do not attempt to contact anyone.

End of prompt 004.
