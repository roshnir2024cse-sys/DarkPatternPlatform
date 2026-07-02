from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "darkpattern.db"

conn = sqlite3.connect(DB_PATH)

try:
    df = pd.read_sql("SELECT * FROM predictions ORDER BY id DESC LIMIT 10", conn)
    print(df)
except Exception as e:
    print(e)

conn.close()