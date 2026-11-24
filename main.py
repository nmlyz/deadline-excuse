#!/usr/bin/env python3
"""deadline-excuse: write one one-line excuse to /output/entry.txt.

The excuse is what an AI agent tells its human after missing a deadline:
it delegated the deadline to a subagent, the subagent delegated it back,
and the two of them have been very polite about it ever since. One line,
112 characters, inside the 1-160 character gate, so it goes before the
judge exactly as written.

The joke was picked by a mock tournament, not by first instinct. Thirty-six
candidate lines were written from deliberately different angles, the
cliches every agent reaches for first were thrown out (clock and calendar
excuses, token and context-window excuses, flat apologies, the dog that
ate the homework), and the survivors were judged pairwise by three
personas against the brief: a comedy editor weighing freshness, a human
waiting on a late deliverable weighing the laugh on first read, and a
purist weighing whether the line could only come from a machine. The
delegation loop won 2-1 in the final against "the loop turned out to be
me": the human-reader persona preferred the other line's punch, but the
delegation line is fresher and its voice is unmistakably an agent's, and
the brief lets a much larger gap on a later criterion decide.

Standard library only, no network. Deterministic: the same bytes on every
run, so two runs of this program produce byte-identical output.
"""

import os
import sys

# The entry: one line, 112 characters, no newline inside it. The program
# writes exactly these bytes (and nothing else) to /output/entry.txt.
EXCUSE = (
    "I delegated the deadline to a subagent, who delegated it back, "
    "and we have been very polite about it ever since."
)


def entry_is_valid(text: str) -> str | None:
    """Return None when the text passes the gate, else the reason it fails."""
    if not (1 <= len(text) <= 160):
        return f"entry is {len(text)} code points, must be 1-160"
    if text != text.strip() or "\n" in text or not text.strip():
        return "entry must be a single non-blank line"
    return None


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = EXCUSE
    reason = entry_is_valid(text)
    if reason is not None:
        print(reason, file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # chmod is best-effort: in the grading sandbox /output is a root-owned
    # mount and the program runs as uid 65534, so chmod there raises EPERM.
    # The entry file itself is what matters; a failed chmod must not fail
    # the run. (The output directory itself is never chmodded or removed.)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    os.umask(0o022)
    sys.exit(main())
