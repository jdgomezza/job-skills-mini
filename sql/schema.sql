CREATE TABLE IF NOT EXISTS job (
  id TEXT PRIMARY KEY,
  title TEXT,
  company TEXT,
  location TEXT,
  url TEXT,
  posted_at TEXT,
  description TEXT
);

CREATE TABLE IF NOT EXISTS skill (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS job_skill (
  job_id TEXT NOT NULL,
  skill_id INTEGER NOT NULL,
  PRIMARY KEY (job_id, skill_id),
  FOREIGN KEY(job_id) REFERENCES job(id),
  FOREIGN KEY(skill_id) REFERENCES skill(id)
);
