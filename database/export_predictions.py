import sqlite3
import pandas as pd

conn = sqlite3.connect("database/darkpattern.db")

df = pd.read_sql("SELECT * FROM predictions", conn)

df.to_csv("database/predictions.csv", index=False)

conn.close()

print("✅ predictions.csv created")