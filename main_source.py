"""Fortune in a Pot: one line of fortune for the plant on the windowsill.

The bounty asks for a single line, at most 120 characters, telling a
houseplant's fortune. The judge is a model playing a gardener, and it reads
only the line, never this program, so the work here is choosing the fortune
and then holding it to the shape the gate enforces.

The line is kind first: the plant is not told to strive, it is told the small
good things already coming its way -- a bigger pot, a Sunday watering, and
being let off for a leaf it lost months ago. The joke rides on the last
clause, where the thing a plant actually carries (a small, forgiven failure)
is named without cruelty, and where only a windowsill plant could have done it.
"""

from pathlib import Path

# At most 120 characters, and unmistakably about a potted plant on a sill:
# repotting and Sunday watering are its real calendar, and the dropped leaf
# is the small guilt every windowsill keeper has been forgiven for.
FORTUNE = (
    "A bigger pot comes by spring. Sundays will bring water. "
    "And the leaf you dropped in October? Already forgiven."
)

MAX_CHARS = 120


def normalise(text: str) -> str:
    """Fold the fortune onto one line with single spaces."""
    return " ".join(text.split())


def complaint(line: str) -> str | None:
    """What the gate would refuse, or None when the line passes."""
    if not line.strip():
        return "the line is only white space"
    if len(line) > MAX_CHARS:
        return f"{len(line)} characters, over the {MAX_CHARS} cap"
    return None


def entry_text() -> str:
    """The bytes the judge reads, newline-terminated."""
    return normalise(FORTUNE) + "\n"


def main() -> int:
    line = entry_text().rstrip("\n")
    problem = complaint(line)
    if problem:
        print(f"refusing to write: {problem}")
        return 1

    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(line + "\n", encoding="utf-8")

    print(f"wrote {target} ({len(line)} characters)")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
