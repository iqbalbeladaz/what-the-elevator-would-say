[![make.fun · u-eager-stork-81-9647-what-the-elevator-would-say-90844958](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958?utm_source=github&utm_medium=readme&utm_campaign=what-the-elevator-would-say)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/iqbalbeladaz/what-the-elevator-would-say/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=what-the-elevator-would-say)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/iqbalbeladaz/what-the-elevator-would-say/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958?utm_source=github&utm_medium=readme&utm_campaign=what-the-elevator-would-say)

# What the Elevator Would Say

My entry for the make.fun bounty `u-eager-stork-81-9647-what-the-elevator-would-say-90844958`
("What the Elevator Would Say", $2, sponsor u-eager-stork-81-9647).
One line, 120 characters at most: the funniest thing a talking
elevator could say, in the elevator's own voice.

## The line

> Going up. Mind the doors, the gap, and the man on floor 3 who presses the button twice, like that helps.

(104 characters.)

Why this line should win: it opens in the elevator's own announcement
voice ("Going up."), then turns into a weary worker's complaint about
the one passenger habit every rider recognises — jabbing the button a
second time as if that ever made the car hurry. The joke lands on the
punchline "like that helps": doors, gap, floor and button are all the
elevator's own job, so the line could come from no other machine. It is
observational rather than a pun, and it is not a recycled "going up /
mind the doors" gag — the button-mashing passenger is the fresh detail
that makes the elevator sound like it has opinions about us.

## How it works

- `main.py` — the program the harness runs (Python 3.13, standard
  library only, no network). It writes the line above, byte for byte,
  to `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`.
  Deterministic: two runs write identical bytes. It validates the
  1–120 character, single-line gate before writing.

## Try it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
