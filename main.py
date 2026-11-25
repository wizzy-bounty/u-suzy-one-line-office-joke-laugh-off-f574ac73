import os

_PARTS = (
    "I asked for a raise",
    "and got a webinar titled 'Owning Your Worth'.",
)
TEXT = " ".join(_PARTS)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
