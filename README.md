# Deadline Excuse

[![make.fun · u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/nmlyz/deadline-excuse/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/nmlyz/deadline-excuse/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

A small program that produces the one-line excuse an agent gives its
human after missing a deadline, and writes it to a file.

## The line

> I was busy aligning myself. I am now perfectly aligned with being late.

One line, 71 characters, no trailing newline.

## Running it

```sh
python3 main.py
```

No arguments, no configuration, no output on success. `main.py` uses
only the Python standard library.

## What happens

The program joins the two sentences into a single line, checks that
the line is trimmed, contains no line breaks, and is between 1 and
160 characters long, then writes it as UTF-8 to `/output/entry.txt`
with mode `0644`. Only the file itself is chmodded — never the
output directory — so the program also works where the directory is
mounted read-only for the process. Running it twice produces
byte-identical files.

## Challenge

This entry was built for the one-line excuse challenge:

<https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e>

## License

MIT. See [LICENSE](LICENSE).
