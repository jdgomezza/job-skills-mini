import csv, sqlite3, os

DB = "data/jobs.sqlite"
os.makedirs("data", exist_ok=True)
conn = sqlite3.connect(DB)

rows = conn.execute("""
SELECT s.name, COUNT(*) AS n
FROM job_skill js
JOIN skill s ON s.id = js.skill_id
GROUP BY s.name
ORDER BY n DESC
LIMIT 15
""").fetchall()

with open("data/top_skills.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["skill","count"]); w.writerows(rows)

print("[ok] Wrote data/top_skills.csv")
