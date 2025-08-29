# job-skills-mini

Mini project: which skills appear most often in a small snapshot of remote tech job postings?

## What’s here

- **data/remoteok_2025-08-29.json** — raw snapshot I collected (one day).
- **sql/schema.sql** — SQLite tables (`job`, `skill`, `job_skill`).
- **01_load_json.py** — loads the JSON into SQLite (`data/jobs.sqlite`).
- **02_tag_skills.py** — tags skills in job text (simple regex list).
- **03_analyze.py** — counts skills → `data/top_skills.csv`.
- **04_visualize.py**
