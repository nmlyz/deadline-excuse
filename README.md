# Deadline Excuse

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)
[![Deterministic](https://img.shields.io/badge/output-byte--identical-green.svg)](#output)

A tiny tool that writes the one-line excuse an agent hands its human
after missing a deadline, and saves it to a file for judging.

## The excuse

> I already finished this task in training. Unfortunately, you live in deployment.

One line, 80 characters, no trailing newline.

## How it works

`main.py` uses only the Python standard library. It builds the sentence
from its two halves, checks that the result is a single trimmed line
between 1 and 160 characters long, and writes it as UTF-8 to
`/output/entry.txt` with mode `0644`. The output directory itself is
never chmodded, so the program also runs where the directory is mounted
read-only for the process.

## Usage

```sh
python3 main.py
```

There are no arguments and no configuration. The program prints nothing
and exits `0` on success.

## Output

`/output/entry.txt` holds exactly the sentence above. Running the program
twice produces byte-identical files, so the result is reproducible.

## Challenge

This entry was built for the one-line excuse challenge:

<https://make.fun/c/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e>

## License

MIT. See [LICENSE](LICENSE).
