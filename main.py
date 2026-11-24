#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line to /output/entry.txt: the dog's own excuse, given
right after being caught with the homework in its mouth.

The line is invented fresh in this session. The dog's logic: the
homework sat on the floor staring at its human for hours, so the
dog did the loyal thing and neutralised the threat first — and,
being a dog, expects thanks rather than trouble for it.
"""

import os

LINE = (
    "It sat on the floor staring at you for three hours, "
    "so I ate it before it could eat you. You're welcome."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
