"""Write the one-line deadline excuse to /output/entry.txt.

The excuse is fixed: two sentences that together make a single line.
The first sentence sets up the agent's excuse, the second turns it
into the punchline. The program joins them, checks the result fits
the challenge's length window and has no line breaks, then stores it
as UTF-8 with no trailing newline.

Run it with:

    python3 main.py

It takes no arguments, prints nothing, and exits 0 on success.
Running it twice leaves byte-identical output behind, so the result
is fully reproducible. Only the Python standard library is used.
"""

import os
import sys

SETUP = "I was busy aligning myself."
PUNCH = "I am now perfectly aligned with being late."

MIN_LENGTH = 1
MAX_LENGTH = 160
OUTPUT_PATH = "/output/entry.txt"


def compose(parts):
    """Join the sentence parts into one line with single spaces."""
    return " ".join(part.strip() for part in parts)


def validate(line):
    """Refuse a line that would fail the challenge's length gate."""
    length = len(line)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError(
            "line is %d characters, allowed %d-%d"
            % (length, MIN_LENGTH, MAX_LENGTH)
        )
    if line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("line must be a single trimmed line")
    return length


def write_entry(line, path):
    """Store the line as UTF-8 bytes, mode 0644 where possible."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(line.encode("utf-8"))
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


def main(argv):
    """Build the excuse, check it, and write it out."""
    del argv  # no command-line options: the excuse is fixed
    line = compose([SETUP, PUNCH])
    validate(line)
    write_entry(line, OUTPUT_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
