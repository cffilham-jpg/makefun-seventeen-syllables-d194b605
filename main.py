import os

HAIKU = """red tests at midnight
a single log line points home
it was a comma
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
