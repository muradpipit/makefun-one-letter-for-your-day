"""One-letter diary entry for make.fun's "One Letter for Your Day" bounty.

The program writes exactly one character to entry.txt: the letter K,
standing for the word "knackered" -- a day that wore me out completely.

Why K: the word behind the letter is what the judge weighs, and
"knackered" is vivid (the picture of someone face-planting on the
sofa after a long day), funny (the word itself lands with a thud),
and true (everyone has had a day like that). K is also not one of
the obvious picks the brief plants -- A for amazing, F for
Friday-feeling, Z for zero sleep -- so it stands out in a field of
letters, and its other natural reading, "killer", is vivid too.
"""

import os
import string

# The word behind the letter, and the letter itself: its initial.
WORD = "knackered"
LETTER = "K"


def main():
    if len(LETTER) != 1 or LETTER not in string.ascii_uppercase:
        raise ValueError("entry must be exactly one letter, A to Z")
    if LETTER != WORD[0].upper():
        raise ValueError("letter must be the initial of the word it stands for")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # The grader collects outputs as another user, so the file must
    # be readable by everyone, whatever the umask is.
    os.chmod(path, 0o644)
    # Read it back: a broken entry must fail loudly here, not sail
    # through to judging with the wrong contents.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if len(written) != 1 or written not in string.ascii_uppercase:
        raise ValueError("entry.txt must hold exactly one letter, A to Z")


if __name__ == "__main__":
    main()
