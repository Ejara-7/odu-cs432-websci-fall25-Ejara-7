# hw2/code/clean_text.py
import os, glob, csv
from boilerpy3 import extractors

RAW_DIR = "hw2/data/raw"
OUT_DIR = "hw2/data/processed"
SUMMARY_CSV = "hw2/data/processed_summary.csv"

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    extractor = extractors.ArticleExtractor()
    rows = []

    files = sorted(glob.glob(os.path.join(RAW_DIR, "*.html")))
    for i, path in enumerate(files, 1):
        stem = os.path.splitext(os.path.basename(path))[0]
        out_path = os.path.join(OUT_DIR, f"{stem}.txt")
        text = ""
        ok = 0
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                html = f.read()
            text = extractor.get_content(html).replace("\r\n", "\n").strip()
            with open(out_path, "w", encoding="utf-8") as out:
                out.write(text)
            ok = 1 if len(text) > 0 else 0
        except Exception:
            open(out_path, "w", encoding="utf-8").close()

        rows.append({"file": f"{stem}.html", "chars": len(text), "nonempty": ok})
        if i % 25 == 0 or i == len(files):
            print(f"[{i}/{len(files)}] processed")

    with open(SUMMARY_CSV, "w", newline="", encoding="utf-8") as sf:
        w = csv.DictWriter(sf, fieldnames=["file","chars","nonempty"])
        w.writeheader()
        w.writerows(rows)

if __name__ == "__main__":
    main()
