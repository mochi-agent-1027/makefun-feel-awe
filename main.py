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


def render():
    """Return the entry text, checked against the competition gate."""
    text = TEXT.strip()
    # The competition gate: UTF-8 text of 1 to 280 code points, not only white space.
    assert 1 <= len(text) <= MAX_CODE_POINTS, "entry text must be 1 to 280 characters"
    assert text == text.strip(), "entry text must not have surrounding white space"
    return text


def main():
    text = render()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Deliberate plain write: the grader reads entry.txt as another user,
    # so the file must keep the default readable mode instead of
    # mkstemp's 0600.
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what was written and verify it matches exactly.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt on disk differs from the rendered text"
    assert 1 <= len(written) <= MAX_CODE_POINTS, "entry.txt must be 1 to 280 characters"


if __name__ == "__main__":
    main()
