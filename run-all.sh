#!/usr/bin/env bash
#
# run-all.sh — chained execution of the missing-scientists research pipeline.
#
# Runs prompts 000 → 001 → 002 → 003 sequentially via Claude Code.
# Each prompt runs in a fresh Claude Code session and communicates with the
# next via the filesystem (the research repo is the shared state).
#
# If any prompt fails (non-zero exit), the chain halts. The `&&` operator
# ensures downstream prompts only run if upstream prompts succeeded.
#
# Does NOT run prompt-004.md — that is the maintenance prompt, invoked
# manually on demand when new information surfaces.
#
# Usage:
#   cd /Users/mnoth/source/research-missing-scientists/
#   ./run-all.sh
#
# Optional: tail a log
#   ./run-all.sh 2>&1 | tee run-all.log

set -euo pipefail

REPO_DIR="/Users/mnoth/source/research-missing-scientists"

if [[ "$(pwd)" != "$REPO_DIR" ]]; then
  echo "ERROR: run this script from $REPO_DIR"
  exit 1
fi

if ! command -v claude &> /dev/null; then
  echo "ERROR: claude CLI not found on PATH. Install Claude Code first."
  exit 1
fi

echo "============================================================"
echo "  Missing Scientists Research Pipeline"
echo "  Starting at: $(date)"
echo "============================================================"
echo ""

echo "--- Running prompt-000 (bootstrap) ---"
claude --dangerously-skip-permissions "$(cat prompt-000.md)" && \

echo "" && \
echo "--- Running prompt-001 (research + artifacts) ---" && \
echo "    This is the long one. May take an hour or more." && \
claude --dangerously-skip-permissions "$(cat prompt-001.md)" && \

echo "" && \
echo "--- Running prompt-002 (PDF generation) ---" && \
claude --dangerously-skip-permissions "$(cat prompt-002.md)" && \

echo "" && \
echo "--- Running prompt-003 (website integration) ---" && \
claude --dangerously-skip-permissions "$(cat prompt-003.md)"

echo ""
echo "============================================================"
echo "  Pipeline complete at: $(date)"
echo "============================================================"

# macOS: audible notification on completion
if command -v say &> /dev/null; then
  say "Research pipeline complete"
fi

# Print a summary of next steps
cat <<EOF

Next steps:
  1. Review STATUS.md for flags or issues.
  2. Review pdf-output/ for generated PDFs.
  3. In /Users/mnoth/source/mattnoth-dev/: the feature branch has been merged
     locally into main but NOT pushed. Review, then 'git push' when ready.
  4. Run prompt-004.md manually when new information surfaces:
     claude --dangerously-skip-permissions "\$(cat prompt-004.md)"

EOF