"""Make the AI Judge Feel Nostalgic: A Childhood Memory (v1).

Writes one original sentence — a childhood memory grounded in a concrete
place, time and sensation — to ``entry.txt`` inside the output directory.

The program is deterministic and offline: no randomness, no network, no
clock, no environment-dependent paths. Every run writes exactly the same
bytes. The sentence is a single sentence of at most 280 characters.
"""

import os
import sys

# One sentence, 212 characters. A kitchen at dusk: steam, rain on the roof,
# a grandmother humming — a small honest moment that keeps echoing.
SENTENCE = (
    "The rice cooker clicked off just as Grandma slid the chipped blue "
    "plate of fried tempeh across the table, and for a second the whole "
    "world was only steam, rain on the zinc roof, and her humming the "
    "same old song."
)

MAX_CHARS = 280


def build_entry() -> str:
    """Return the entry sentence, guarding the competition's length cap."""
    text = SENTENCE.strip()
    if not text:
        raise SystemExit("entry sentence is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry sentence must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry sentence is {len(text)} characters, over the "
            f"{MAX_CHARS} cap"
        )
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(build_entry())


if __name__ == "__main__":
    main()
