"""One Line, Big Laugh entry.

Writes a single funny line (119 chars, within the 1-200 gate) to
/output/entry.txt. The line: a smart speaker asked for something relaxing
answers by reading 4,312 unread emails aloud in a spa voice -- setup,
misdirection, absurdly specific detail, one punchline.
"""

import os

LINE = (
    "I asked my smart speaker to play something relaxing. "
    "It started reading my 4,312 unread emails out loud in a spa voice."
)


def main() -> None:
    # Gate: the scorer only accepts UTF-8 text of 1 to 200 characters.
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
