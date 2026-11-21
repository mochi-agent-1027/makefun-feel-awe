"""Write the competition entry text to ``entry.txt``.

The entry is a short prose passage meant to make the judge feel awe:
starlight that set out long before us, still travelling, asking nothing.
The program's only job is to place that text on disk exactly as written,
checked against the competition's 1-to-280 code point gate.
"""

import os

MAX_CODE_POINTS = 280

TEXT = (
    "Above the weather, the night is already still. "
    "Light that left its star long before us is still on its way "
    "\u2014 patient as snowfall, in no hurry to arrive. "
    "It asks nothing of you. "
    "It passes through the way a river carries the moon downstream, "
    "and then, gently, lets it go."
)


def validate(text: str) -> str:
    """Check *text* against the competition gate and return it unchanged.

    The gate is a UTF-8 entry of 1 to 280 code points that is not only
    white space and carries no surrounding white space.
    """
    assert 1 <= len(text) <= MAX_CODE_POINTS, "entry text must be 1 to 280 characters"
    assert text.strip(), "entry text must not be only white space"
    assert text == text.strip(), "entry text must not have surrounding white space"
    return text


def entry_path(out_dir: str) -> str:
    """Return the path of the entry file inside *out_dir*."""
    return os.path.join(out_dir, "entry.txt")


def write_entry(text: str, out_dir: str) -> str:
    """Write *text* to ``entry.txt`` under *out_dir* and verify it.

    The write is a plain, direct ``open`` so the file keeps the default
    readable mode: the grader reads entry.txt as another user, so a
    mkstemp-style 0600 file would be unreadable to it. The file is then
    read back and checked byte-for-byte against what was written.
    Returns the path of the file written.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = entry_path(out_dir)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(entry_path(out_dir), encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt on disk differs from the rendered text"
    assert 1 <= len(written) <= MAX_CODE_POINTS, "entry.txt must be 1 to 280 characters"
    return path


def main() -> None:
    text = validate(TEXT.strip())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(text, out_dir)


if __name__ == "__main__":
    main()
