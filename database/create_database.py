from pathlib import Path
import sqlite3
import pandas as pd

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
csv_path = BASE_DIR / "dataset" / "final_output.csv"
db_path = BASE_DIR / "database" / "darkpattern.db"

# Read CSV
df = pd.read_csv(csv_path)

# Connect SQLite
conn = sqlite3.connect(db_path)

# Save CSV to SQLite
df.to_sql(
    "amazon_products",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()
conn.close()

print("✅ Database created successfully!")