import csv, os
import matplotlib.pyplot as plt

skills, counts = [], []
with open("data/top_skills.csv", encoding="utf-8") as f:
    r = csv.DictReader(f)
    for row in r:
        skills.append(row["skill"])
        counts.append(int(row["count"]))

os.makedirs("figs", exist_ok=True)

plt.figure(figsize=(9,4))             
plt.bar(skills, counts)               
plt.title("Top skills in remote job postings (snapshot)")
plt.xlabel("Skill")
plt.ylabel("Job count")
plt.xticks(rotation=45, ha="right")   
plt.tight_layout()                    

plt.savefig("figs/top_skills.png", dpi=200)
print("[ok] Saved figs/top_skills.png")
