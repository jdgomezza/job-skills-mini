import json, sqlite3, os

DATA = "data/remoteok_2025-08-29.json"
DB   = "data/jobs.sqlite"

def normalize(item: dict) -> dict:
    return {
        "id": str(item.get("id") or item.get("url")),
        "title": item.get("position") or "",
        "company": item.get("company") or "",
        "location": item.get("location") or "",
        "url": item.get("url") or "",
        "posted_at": item.get("date") or "",
        "description": (item.get("description") or "")[:20000]
    }

def main():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB)
    conn.executescript(open("sql/schema.sql", encoding="utf-8").read())

    data = json.load(open(DATA, encoding="utf-8"))
    jobs = [normalize(x) for x in data[1:] if isinstance(x, dict)]

    for j in jobs:
        conn.execute("""
          INSERT OR REPLACE INTO job(id,title,company,location,url,posted_at,description)
          VALUES(:id,:title,:company,:location,:url,:posted_at,:description)
        """, j)
    conn.commit()
    print(f"[ok] {len(jobs)} Jobs loaded into database")
    conn.close()

if __name__ == "__main__":
    main()
