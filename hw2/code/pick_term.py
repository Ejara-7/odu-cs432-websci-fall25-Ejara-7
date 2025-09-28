# hw2/code/pick_term.py
# Find candidate terms that appear in at least 10 different documents.

import os, re, glob
from collections import defaultdict

PROCESSED_DIR = "hw2/data/processed"

# simple built-in stopword list (avoid pulling extra packages)
STOPWORDS = {
    "the","of","and","to","in","a","for","is","on","that","with","as","by","this",
    "be","are","or","an","from","at","it","we","you","your","our","their","was",
    "were","have","has","had","not","but","will","can","may","if","about","more",
    "into","out","all","any","other","which","also","these","those","than",
    "http","https","www","com","org","edu","amp"
}

TOKEN = re.compile(r"[A-Za-z]+")

def tokens(text):
    return [t.lower() for t in TOKEN.findall(text)]

def main():
    df = defaultdict(int)  # document frequency: term -> #docs containing it
    files = glob.glob(os.path.join(PROCESSED_DIR, "*.txt"))
    for path in files:
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except:
            continue
        terms = set(t for t in tokens(text) if len(t) >= 3 and t not in STOPWORDS)
        for t in terms:
            df[t] += 1

    # show candidates appearing in >= 10 docs (sorted high->low)
    candidates = [(count, term) for term, count in df.items() if count >= 10]
    candidates.sort(reverse=True)
    print(f"Found {len(candidates)} terms that appear in >= 10 docs.")
    print("Top 50 candidates:")
    for count, term in candidates[:50]:
        print(f"{term:20s}  {count}")

if __name__ == "__main__":
    main()
