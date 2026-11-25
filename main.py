"""One Star for Monday — make.fun bounty entry.

Writes a single line of plain text to /output/entry.txt: a one-star
review of Monday, written as though Monday were a restaurant.
At most 25 words, no explanation attached.
"""

import os

ENTRY = (
    "One star. They seated me at 7am, served cold coffee, and billed me "
    "my entire weekend. Never eating at Monday again."
)

MAX_WORDS = 25
MAX_CHARS = 180


def write_entry(output_dir):
    """Write the review line to entry.txt inside output_dir."""
    words = ENTRY.split()
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError("entry must be 1-180 characters, got %d" % len(ENTRY))
    if len(words) > MAX_WORDS:
        raise ValueError("entry must be at most 25 words, got %d" % len(words))
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(output_dir)
    print("wrote %s (%d words, %d chars)" % (path, len(ENTRY.split()), len(ENTRY)))


if __name__ == "__main__":
    main()
