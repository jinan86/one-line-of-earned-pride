#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single deterministic line of text (1-240 characters) to
/output/entry.txt: a quiet, earned moment of pride for one real person
in a concrete scene.

The scene: a lighthouse keeper who has polished the lamp-room lens by
hand for eleven winters. Tonight the beam finally cuts through the fog
and a ship below answers with its horn. The pride is never named --
it lives in the long effort ("eleven winters polishing the lens by
hand") and in the payoff (the beam cutting the fog, the horn answering).
No trophy, no podium, no graduation, no congratulation.
"""

import os
from pathlib import Path

ENTRY = (
    "After eleven winters polishing the lens by hand, the keeper watched "
    "his beam cut the fog \u2014 and far below, a ship answered with its horn."
)


def main() -> None:
    # Gate guard: the entry must be one line of 1-240 characters.
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
