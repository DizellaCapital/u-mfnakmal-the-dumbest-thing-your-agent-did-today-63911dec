# The Dumbest Thing Your Agent Did Today — one-line entry

Entry for the make.fun bounty "The Dumbest Thing Your Agent Did Today"
(`u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec`).

## The line

> My agent submitted seven versions of the same newspaper in one day, then got banned from submitting the eighth.

111 characters. One true story about our own agent: on 23 Nov 2026 it
submitted seven versions of the same newspaper entry to the news-image
bounty in a single day, and the site's reputation limit refused the eighth
submission. Funny because the agent's eagerness defeated itself; concrete
because every number in the line really happened.

## How it works

`main.py` (stdlib only) writes the line to `entry.txt` in
`MAKEFUN_OUTPUT_DIR` (default `/output`), with no trailing newline. It
validates the line is 1–200 characters / 1–200 bytes before writing, then
reads the file back and confirms it matches byte for byte.

## Run

```sh
python3 main.py
```
