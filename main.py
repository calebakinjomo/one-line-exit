"""The One-Line Exit — a one-line resignation letter.

The program writes the entry line to /output/entry.txt (the path the
make.fun program/v1 harness grades) and prints exactly the same line.

The joke lands by treating a corporate "we are family" slogan as a
literal household to flee — a resignation framed as running away from home.
"""

import os

ENTRY = "I hereby resign: after two years of being told we are a family, I have decided to finally run away from home."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
