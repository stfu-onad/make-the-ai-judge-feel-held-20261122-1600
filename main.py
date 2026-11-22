"""make-the-ai-judge-feel-held-20261122-1600.

Writes one short relaxing text to /output/entry.txt.
No network, no input, deterministic output.
"""

import os

TEXT = (
    # One image, held still: a hammock keeping its shape for no one,
    # a breeze checking that everything is where it should be.
    # No instruction to relax anywhere in it — the calm is the scene.
    "Between two old trees, the hammock holds its curve even empty, "
    "its ropes gone soft with years of afternoons. A breeze passes "
    "through it like someone checking, once, that everything is still "
    "where it should be."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
