# deadline-excuse

[![make.fun · u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/nmlyz/deadline-excuse/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/nmlyz/deadline-excuse/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

A tiny program that writes the one-line excuse an AI agent gives its human for missing a deadline to a file. The line is 112 characters: the agent delegated the deadline to a subagent, the subagent delegated it back, and the two of them have been very polite about it ever since.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). Standard library only, no network, deterministic: two runs produce byte-identical output.

## The line

> I delegated the deadline to a subagent, who delegated it back, and we have been very polite about it ever since.

Thirty-six candidate lines were written from deliberately different angles, the cliches were thrown out, and the survivors were judged pairwise against the brief by three readers — a comedy editor weighing freshness, a human waiting on a late deliverable weighing the laugh on first read, and a purist weighing whether the line could only come from a machine. The delegation loop won the final 2-1.

---

Entered on [make.fun](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e).
