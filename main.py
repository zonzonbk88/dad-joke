"""Dad Joke Showdown entry.

Writes a single dad joke (one line, at most 200 characters) to
/output/entry.txt. Standard library only.
"""

import os

JOKE = "I told my wife to embrace her mistakes. She gave me a hug."


def main() -> None:
    # Enforce the competition gate before writing: 1-200 chars, one line.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only white space"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
