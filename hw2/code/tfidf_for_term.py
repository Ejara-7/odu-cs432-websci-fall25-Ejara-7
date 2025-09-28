# hw2/code/tfidf_for_term.py
# Usage example:
#   py hw2\code\tfidf_for_term.py "privacy" --df_web 123456789 --web_size 40000000000 --top 10

import os, re, csv, glob, math, argparse
from urllib.parse import urlparse

PROCESSED_DIR = "hw2/data/processed"
MAPPING_CSV   = "hw2/data/mapping.csv"
OUT_CSV       = "hw2/data/tfidf_results.csv"

TOKEN = re.compile(r"[A-Za-z]+")

def tokenize(text):
    return [t.lower() for t in TOKEN.findall(text)]

def load_mapping():
    # returns dict: hash (no .html/.txt) -> uri
    m = {}
    with open(MAPPING_CSV, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            m[row["hash"]] = row["uri"]
    return m

def domain_of(uri: str) -> str:
    try:
        return urlparse(uri).hostname or ""
    except:
        return ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("term", help="query term (case-insensitive exact token match)")
    ap.add_argument("--df_web", type=float, required=True, help="search engine result count for the term")
    ap.add_argument("--web_size", type=float, default=40_000_000_000, help="N: total web size (Google=40B, Bing=4B)")
    ap.add_argument("--top", type=int, default=10, help="how many results to keep (distinct domains)")
    args = ap.parse_args()

    term = args.term.lower()
    df_web = max(1.0, args.df_web)     # avoid divide-by-zero
    N = max(df_web, args.web_size)     # N should be >= df_web

    # IDF with log base 2
    idf = math.log2(N / df_web)

    mapping = load_mapping()

    rows = []
    files = glob.glob(os.path.join(PROCESSED_DIR, "*.txt"))
    for path in files:
        stem = os.path.splitext(os.path.basename(path))[0]  # hash without extension
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except:
            continue

        toks = tokenize(text)
        total_words = len(toks)
        if total_words == 0:
            continue
        term_count = sum(1 for t in toks if t == term)
        if term_count == 0:
            continue

        tf = term_count / total_words
        tfidf = tf * idf
        uri = mapping.get(stem, f"(no-uri-for-{stem})")
        rows.append({
            "tfidf": tfidf,
            "tf": tf,
            "idf": idf,
            "term_count": term_count,
            "total_words": total_words,
            "hash": stem,
            "uri": uri,
            "domain": domain_of(uri)
        })

    # sort by TF-IDF descending
    rows.sort(key=lambda r: r["tfidf"], reverse=True)

    # keep distinct domains
    picked, seen_domains = [], set()
    for r in rows:
        d = r["domain"]
        if d and d not in seen_domains:
            picked.append(r)
            seen_domains.add(d)
        if len(picked) >= args.top:
            break

    # save CSV (nice to include in repo)
    fieldnames = ["tfidf","tf","idf","term_count","total_words","uri","domain","hash"]
    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in picked:
            w.writerow({k: r[k] for k in fieldnames})

    # also print a Markdown table you can paste into the report
    print("\nMarkdown table for your report:")
    print("| TF-IDF | TF | IDF | URI |")
    print("|-------:|----:|-----:|-----|")
    for r in picked:
        print(f"| {r['tfidf']:.3f} | {r['tf']:.4f} | {r['idf']:.3f} | {r['uri']} |")
    print("\nSaved CSV:", OUT_CSV)

if __name__ == "__main__":
    main()
