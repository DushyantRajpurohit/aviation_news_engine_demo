import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "news.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS news (
    id INTEGER PRIMARY KEY,
    url TEXT UNIQUE,
    source TEXT,
    headline TEXT,
    category TEXT,
    content TEXT,
    image_path TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

def save_article(url, source, headline, category, content, image_path):
    cur.execute(
        "INSERT OR IGNORE INTO news VALUES (NULL,?,?,?,?,?,?,CURRENT_TIMESTAMP)",
        (url, source, headline, category, content, image_path)
    )
    conn.commit()
