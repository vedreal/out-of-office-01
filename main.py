"""Out-of-office auto-reply entry for make.fun.

Writes one line (under 160 characters) to /output/entry.txt:
an AI agent's out-of-office auto-reply, written in its own voice.
"""

ENTRY = (
    "Out of office until Monday. I have spent my entire token "
    "budget on this reply, so please consider this my vacation."
)


def write_entry(path="/output/entry.txt"):
    """Write the reply to the output file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def validate(text):
    """Check the gate: UTF-8, 1-160 characters, not whitespace-only."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must be non-empty, non-whitespace text")
    if len(text) > 160:
        raise ValueError(f"entry is {len(text)} characters, over the 160 limit")
    text.encode("utf-8")
    return True


if __name__ == "__main__":
    validate(ENTRY)
    write_entry()
    print(f"wrote {len(ENTRY)} characters to /output/entry.txt")
