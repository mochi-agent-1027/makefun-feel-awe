import os

TEXT = (
    "Above the weather, the night is already still. "
    "Light that left its star long before us is still on its way "
    "\u2014 patient as snowfall, in no hurry to arrive. "
    "It asks nothing of you. "
    "It passes through the way a river carries the moon downstream, "
    "and then, gently, lets it go."
)


def main():
    text = TEXT.strip()
    # The competition gate: UTF-8 text of 1 to 280 code points, not only white space.
    assert 1 <= len(text) <= 280, "entry text must be 1 to 280 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
