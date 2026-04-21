# Runbook — Missing Scientists Research Pipeline

This is a living-artifact research project. The pipeline is composed of five prompts (000–004), executed via Claude Code CLI.

## Prompts at a glance

### Build prompts (`prompts/build/`)

| Prompt | Purpose | Runs in chain? | Typical duration |
|---|---|---|---|
| `prompts/build/prompt-000.md` | Bootstrap: initialize git repo, create skeleton, write README stub | Yes | ~1 min |
| `prompts/build/prompt-001.md` | Main research: spawn sub-agents, populate case files, appendices, analysis, data JSON | Yes | ~1–2 hours |
| `prompts/build/prompt-002.md` | PDF generation (dossier, cases, diagrams, timeline) | Yes | ~10–20 min |
| `prompts/build/prompt-003.md` | Website integration in `/Users/mnoth/source/mattnoth-dev/` | Yes | ~30–60 min |
| `prompts/build/prompt-resume.md` | Resume after rate-limit interruption | Manual | Variable |
| `prompts/build/prompt-reconcile.md` | Audit interrupted prompt-001 for completeness | Manual | ~10 min |

### News update prompt (top-level)

| Prompt | Purpose | Runs in chain? | Typical duration |
|---|---|---|---|
| `prompt-004.md` | Maintenance / update — run manually when news surfaces | No (manual) | Variable |

### Deep research prompts (`prompts/research/`)

| Prompt | Purpose | Depends on | Typical duration |
|---|---|---|---|
| `prompt-deep-001.md` | Public records & primary source deep dive (11 sub-agents, 1 per case) | — | ~1–2 hours |
| `prompt-deep-002.md` | Professional networks: patents, publications, grants, associations (4 sub-agents) | — | ~1 hour |
| `prompt-deep-003.md` | Foreign-language & international source expansion (5 regional sub-agents) | — | ~1 hour |
| `prompt-deep-004.md` | Historical precedent & base-rate statistical analysis (3 sub-agents) | — | ~1 hour |
| `prompt-deep-005.md` | Integration, comparison & gap audit — updates analysis, data, dossier | 001–004 | ~30–60 min |

See `prompts/research/README.md` for alignment rules and execution details.

## Running the chain

### Full pipeline (fresh run)

```bash
cd /Users/mnoth/source/research-missing-scientists/
chmod +x run-all.sh    # first time only
./run-all.sh 2>&1 | tee run-all.log
```

### Output model

The script uses `claude -p --output-format=stream-json --verbose`, which emits every event — assistant text, thinking blocks, tool calls, tool results — as JSON. A `jq` filter in the script pretty-prints these to your terminal in real time with color coding:

- `[thinking]` (grey) — the agent's reasoning
- `[assistant]` (cyan) — text the agent generated
- `[tool: name]` (yellow) — tool invocations (web_search, bash, create_file, etc.)
- `[tool result]` (green) — what the tool returned (truncated to 500 chars for readability)
- `[done]` (magenta) — end-of-prompt summary

The **raw JSON** is always captured in `run-all-raw.log` regardless of terminal output. Useful for later analysis, debugging, or re-running the jq filter:

```bash
cat run-all-raw.log | jq -r 'select(.type=="assistant") | .message.content[] | select(.type=="text").text'
```

### Dependencies

- **`jq`** — strongly recommended for readable output. `brew install jq`. If missing, the script warns and falls back to raw JSON (still captured, just noisier in the terminal).
- **`claude`** — Claude Code CLI. `claude --version` should report a current version.

### One-liner equivalent (manual, no script)

```bash
cd /Users/mnoth/source/research-missing-scientists/ && \
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-000.md)" && \
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-001.md)" && \
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-002.md)" && \
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-003.md)"
```

(Without `jq` piping, you get raw JSON. Use the script for the filtered view.)

### Running a single prompt

```bash
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-001.md)"
```

Or with the same pretty-printing the script uses:

```bash
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-001.md)" | jq -r '
  select(.type != "system") |
  if .type == "assistant" then
    (.message.content // [])[] |
    if .type == "text" then "\n[assistant] " + .text
    elif .type == "thinking" then "\n[thinking] " + (.thinking // "")
    elif .type == "tool_use" then "\n[tool: " + .name + "] " + ((.input // {}) | tostring)
    else empty end
  elif .type == "user" then
    (.message.content // [])[] |
    if .type == "tool_result" then "\n[tool result] " + ((.content // "") | tostring)
    else empty end
  elif .type == "result" then "\n[done] " + (.result // "")
  else empty end
'
```

### Maintenance updates

```bash
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompt-004.md)"
```

### Deep research prompts

Run any of prompts deep-001 through deep-004 independently (any order), then run deep-005 to integrate:

```bash
# Example: run primary source deep dive
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/research/prompt-deep-001.md)"

# After all deep dives complete, integrate
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/research/prompt-deep-005.md)"
```

Pipe through `jq` as above if you want pretty output.

### Monitoring progress from another terminal

While the chain runs, a second terminal can watch progress directly via the repo filesystem — often more useful than scrolling output:

```bash
cd /Users/mnoth/source/research-missing-scientists

# Commits as they land
watch -n 5 'git log --oneline | head -15'

# The agent's own research log as it grows
tail -f logs/research-log.md

# Case files appearing
watch -n 10 'ls -la cases/'

# Everything at once (if you have `watch` and a wide terminal)
watch -n 5 'git log --oneline | head -5; echo; ls cases/ 2>/dev/null | wc -l | xargs echo "cases written:"; echo; tail -5 logs/research-log.md 2>/dev/null'
```

### Background run (close terminal, return later)

```bash
nohup ./run-all.sh > run-all.log 2>&1 &
echo "Started as PID $!"

# Watch anytime:
tail -f run-all.log
```

The `say "Research pipeline complete"` at the end speaks through your Mac speakers when done regardless of whether you're watching.

## Safety model

Every prompt follows the same hard rules:

- **Scope:** only the research repo (and `mattnoth-dev/` in prompt 003 only).
- **Pre-approved silent installs:** pandoc, weasyprint (via `brew`), d3 + @types/d3 and markdown-it (via `npm` local to `mattnoth-dev/`). Any other install requires the agent to stop and ask.
- **No `sudo`. Never.**
- **No git push.** Agents commit locally only. You push.
- **No contact attempts.** Agents do not email, message, submit forms, or reach out to any person, family, agency, or reporter.
- **No arbitrary network access** beyond Claude Code's web search/fetch tools, `git` local operations, and the pre-approved package managers.

If an agent is unsure whether an action is in scope, it stops and asks. In practice this should be rare — the prompts are designed to run unattended end-to-end.

## Prompt authoring permissions

Every prompt in the series may:
- **Alter downstream prompts** for correctness (missing context, structural conflicts, incorrect state assumptions). Never for stylistic preference.
- **Create new prompts** if a task decomposes better than the current structure. New prompts use logical numbering (e.g., `prompt-001a.md` for insertions, `prompt-005.md` for additions).

Every alteration and creation is logged in `logs/prompt-alterations.md` with filename, what changed, why, and date. When a new prompt enters the chain, the agent updates `run-all.sh` and this RUNBOOK to reflect the change. Review `logs/prompt-alterations.md` after every run to see what the agent decided.

## Reviewing the output

After the chain completes:

1. **`STATUS.md`** at the research repo root — read first. Summarizes what was produced, what was skipped, any flags for review.
2. **`CHANGELOG.md`** — version history.
3. **`logs/research-log.md`** — chronological log of what sub-agents searched and found, including dead ends.
4. **`logs/contradictions.md`** — tracked source-to-source disagreements.
5. **`logs/known-unknowns.md`** — gaps the research could not resolve, with specificity.
6. **`dossier.md`** — the main artifact. Start with the abstract and executive summary.
7. **`pdf-output/`** — generated PDFs (dossier, per-case, diagrams, timeline).
8. **Website:** check out the `feature/missing-scientists` branch in `mattnoth-dev/` (now merged to main, not pushed). Build and view locally.

## Pushing the website

Prompts do not push. When you're satisfied with the website:

```bash
cd /Users/mnoth/source/mattnoth-dev/
git status              # confirm you're on main with the merge
git log --oneline -5    # confirm the feature branch merge is there
git push origin main    # push when ready
```

## Regenerating after updates

If you run `prompt-004.md` and it changes the research:

- **PDFs are out of date:** run `prompt-002.md`.
- **Website is out of date:** run `prompt-003.md`.

Prompt 004 will ask whether to regenerate these. You can say yes/no case by case.

## Known limitations

- **Paywalled foreign coverage** (e.g., some major international outlets behind subscription walls): documented in `logs/known-unknowns.md`. The research does not bypass paywalls; it looks for syndicated reposts and notes when those are not available.
- **Claims requiring comment from named individuals or agencies:** never solicited. The research works only from already-public material.
- **Evolving investigations:** cases resolve, new cases surface, House Oversight will likely release findings. The `prompt-004.md` workflow handles updates; rerun it when material new information surfaces.

## Tips

- The `run-all.sh` script writes `run-all-raw.log` unconditionally — the raw stream-json from every prompt in the chain. This is your authoritative transcript. Add it to `.gitignore` if you don't want it tracked (it can get large).
- If running overnight, redirect pretty output to a log and run in background:
  ```bash
  nohup ./run-all.sh > run-all.log 2>&1 &
  ```
  Then `tail -f run-all.log` when you want to peek.
- If prompt 001 fails partway through, you can often re-invoke it — the prompt is designed to be idempotent for completed case files (sub-agents will see existing files and not redo them). Check `logs/research-log.md` first to confirm state. Alternatively, use `prompts/build/prompt-resume.md` or `prompts/build/prompt-reconcile.md`.
- **Re-reading the reasoning after a run:** the raw log preserves every thinking block, tool call, and tool result. You can grep it freely. For example, to see every `web_search` query the agent ran:
  ```bash
  jq -r 'select(.type=="assistant") | .message.content[]? | select(.type=="tool_use" and .name=="web_search") | .input.query' run-all-raw.log
  ```
  Or every file created:
  ```bash
  jq -r 'select(.type=="assistant") | .message.content[]? | select(.type=="tool_use" and .name=="create_file") | .input.path' run-all-raw.log
  ```
- The research repo is the source of truth. Website and PDFs are renderings. If you want to edit content, edit the markdown in the research repo, then regenerate — don't edit the PDFs or the website HTML directly.