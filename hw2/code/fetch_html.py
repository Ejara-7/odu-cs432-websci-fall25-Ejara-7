# hw2/code/fetch_html.py
import csv, hashlib, os, time, requests, sys

INPUT_URIS = "hw2/data/uris.txt"   # change if your file is named differently
RAW_DIR    = "hw2/data/raw"
MAP_CSV    = "hw2/data/mapping.csv"

def md5_hex(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()

def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    with open(INPUT_URIS, "r", encoding="utf-8") as f:
        uris = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

    headers = {"User-Agent": "ODU-CS432-HW2/1.0 (student project)"}
    rows = []

    for i, uri in enumerate(uris, start=1):
        h = md5_hex(uri)
        out_path = os.path.join(RAW_DIR, f"{h}.html")
        status = ""
        ok = False
        try:
            resp = requests.get(uri, headers=headers, timeout=15, allow_redirects=True)
            status = str(resp.status_code)
            if resp.ok:
                text = (resp.text or "").replace("\r\n", "\n")
                with open(out_path, "w", encoding=resp.encoding or "utf-8", errors="ignore") as out:
                    out.write(text)
                ok = True
            else:
                open(out_path, "w", encoding="utf-8").close()
        except Exception as e:
            status = f"ERROR:{type(e).__name__}"
            open(out_path, "w", encoding="utf-8").close()

        rows.append({"idx": i, "uri": uri, "hash": h, "status": status, "ok": "1" if ok else "0"})
        print(f"[{i}/{len(uris)}] {uri} -> {h}.html  status={status} ok={ok}")
        time.sleep(0.5)  # be polite

    with open(MAP_CSV, "w", newline="", encoding="utf-8") as mf:
        w = csv.DictWriter(mf, fieldnames=["idx","uri","hash","status","ok"])
        w.writeheader()
        w.writerows(rows)

if __name__ == "__main__":
    # Optional: run a small test subset if you create hw2/data/uris_small.txt
    if len(sys.argv) == 2 and sys.argv[1] == "--small":
        INPUT_URIS = "hw2/data/uris_small.txt"
    main()
