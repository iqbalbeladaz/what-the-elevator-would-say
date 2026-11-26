#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun bounty
u-eager-stork-81-9647-what-the-elevator-would-say-90844958.

The program the harness runs (Python 3.13, standard library only, no
network). It writes the entry line, byte for byte, to
$MAKEFUN_OUTPUT_DIR/entry.txt, defaulting to /output/entry.txt.
Deterministic: two runs write identical bytes.

The line (104 characters; the gate needs 1-120, one line, in the
elevator's own voice):
    Going up. Mind the doors, the gap, and the man on floor 3 who
    presses the button twice, like that helps.

Why this line: it opens in the elevator's own announcement voice
("Going up."), then turns into a weary worker's complaint about the
one passenger habit every rider recognises — jabbing the button a
second time as if that ever made the car hurry. The joke lands on the
punchline "like that helps": doors, gap, floor and button are all the
elevator's own job, so the line could come from no other machine; it
is observational rather than a pun, and it is not a recycled "going
up / mind the doors" gag — the button-mashing passenger is the fresh
detail that makes the elevator sound like it has opinions about us.
"""

import os

LINE = "Going up. Mind the doors, the gap, and the man on floor 3 who presses the button twice, like that helps."


def main() -> None:
    # The gate refuses anything outside 1-120 characters; fail loudly here
    # rather than shipping an entry the scorer would list as invalid.
    if not 1 <= len(LINE) <= 120 or not LINE.strip():
        raise SystemExit(f"entry line is {len(LINE)} characters; gate needs 1-120")
    if "\n" in LINE:
        raise SystemExit("entry must be a single line")
    if LINE != LINE.strip():
        # The gate counts every character, so a stray leading or trailing
        # space would eat budget and change the judged text.
        raise SystemExit("entry must not have leading or trailing whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
