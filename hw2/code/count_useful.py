# hw2/code/count_useful.py
import os, glob

PROC_DIR = "hw2/data/processed"

def main():
    files = glob.glob(os.path.join(PROC_DIR, "*.txt"))
    total = len(files)
    nonempty = 0
    for p in files:
        try:
            if os.path.getsize(p) > 0:
                nonempty += 1
        except OSError:
            pass
    pct = (100.0 * nonempty / total) if total else 0.0
    print(f"Processed text files: {total}")
    print(f"Non-empty processed files: {nonempty}")
    print(f"Percent non-empty: {pct:.1f}%")

if __name__ == "__main__":
    main()
