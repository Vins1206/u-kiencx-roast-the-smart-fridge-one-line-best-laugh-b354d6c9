"""Roast the Smart Fridge: one line, best laugh wins.

Writes exactly one roast line (at most 160 characters) to
/output/entry.txt. Python stdlib only.
"""

from pathlib import Path

ROAST = (
    "My smart fridge updated itself overnight and now its touchscreen "
    "is just a $3,000 whiteboard that hums and judges my leftovers."
)


def main() -> None:
    text = " ".join(ROAST.split())
    assert 1 <= len(text) <= 160, f"roast is {len(text)} chars, must be 1-160"
    assert text.count("\n") == 0, "roast must be exactly one line"
    # One sentence only: a single terminal period, no second sentence.
    assert text.endswith(".") and text.count(".") == 1, "roast must be one sentence"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
