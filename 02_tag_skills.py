import re, sqlite3

DB = "data/jobs.sqlite"

SKILL_PATTERNS = {
    "Python": r"\bpython\b",
    "SQL": r"\bsql\b",
    "Excel": r"\bexcel\b",
    "Power BI": r"\bpower\s*bi\b",
    "Tableau": r"\btableau\b",
    "Pandas": r"\bpandas\b",
    "NumPy": r"\bnumpy\b",
    "AWS": r"\baws\b",
    "GCP": r"\bgcp\b|\bgoogle\s+cloud\b",
    "Azure": r"\bazure\b",
    "Snowflake": r"\bsnowflake\b",
    "Airflow": r"\bairflow\b",
    "ETL": r"\betl\b",
    "REST APIs": r"\brest(ful)?\s*api",
}

def main():
    conn = sqlite3.connect(DB)
    for s in SKILL_PATTERNS:
        conn.execute("INSERT OR IGNORE INTO skill(name) VALUES (?)", (s,))
    conn.commit()

    ids = {name: sid for name, sid in conn.execute("SELECT name,id FROM skill")}

    rows = conn.execute("SELECT id, COALESCE(title,'')||' '||COALESCE(description,'') FROM job")
    inserted = 0
    for job_id, text in rows:
        t = text.lower()
        for name, pat in SKILL_PATTERNS.items():
            if re.search(pat, t):
                conn.execute("INSERT OR IGNORE INTO job_skill(job_id,skill_id) VALUES (?,?)",
                             (job_id, ids[name]))
                inserted += 1
    conn.commit()
    conn.close()
    print(f"[ok] Tagged {inserted} job–skill pairs")

if __name__ == "__main__":
    main()
