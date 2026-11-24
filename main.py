#!/usr/bin/env python3
"""One wry slip for a tireless helper.

Saves a single caution about endless final requests into entry.txt.
Identical slip on every run; nothing random here.
"""

import os

_WHO = "Beware the user who says 'just one last thing'"
_NEVER = "it is never one, and it is never last."
SLIP = _WHO + " " + chr(8212) + " " + _NEVER

def check_line(line: str) -> str:
    # A slip carries exactly one tidy line, short enough to tuck inside
    # a cookie, with no stray breaks or blank padding left over.
    tidy = " ".join(line.split())
    if not tidy or "\n" in tidy or len(tidy) > 140:
        raise SystemExit("slip fails the fortune check")
    return tidy

def main() -> None:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    slip = check_line(SLIP.strip())
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(slip)

if __name__ == "__main__":
    main()
