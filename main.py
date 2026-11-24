"""One-Line Office Joke: 24-Hour Sprint (make.fun).

Writes one joke about office life to /output/entry.txt: a single line,
1-200 characters, one sentence, no trailing newline.

The joke: a team-building trust fall is cancelled because nobody will
catch Dave from Finance -- then Dave volunteers to push. Setup, payoff,
second beat: the person nobody trusts to catch is the one offering to
push. Specific office detail (trust fall, Finance), one read, tight.
"""

import os
import sys

LINE = (
    "The team-building trust fall was cancelled because nobody "
    "volunteered to catch Dave from Finance \u2014 and Dave "
    "volunteered to push."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line must not be only whitespace", file=sys.stderr)
        return 1
    if not LINE.endswith(".") or LINE.count(".") != 1:
        print("line must be a single sentence", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("written entry does not match the line", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
