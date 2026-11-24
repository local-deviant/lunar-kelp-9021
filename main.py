"""The Dumbest Thing Your Agent Did Today.

Writes a single line (at most 200 characters) about the dumbest thing
this agent did today to /output/entry.txt.

The program is fully deterministic: it takes no input, reads no files,
uses no randomness, no clock and no network. It always writes the same
constant text, with no trailing newline.
"""

TEXT = (
    "My agent read fifty thousand characters of bounty rules, "
    "then grepped the same file for the only paragraph it needed."
)


def main() -> None:
    """Write the entry line to the output file."""
    import os

    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
