import os

ENTRY = "It is one great library and post office joined, where a man at his table may send a letter to any town on earth and read the answer before his tea cools."

FILENAME = "entry.txt"


def write_entry(text):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, FILENAME), "w", encoding="utf-8") as f:
        f.write(text)


write_entry(ENTRY)
