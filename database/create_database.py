import sqlite3
import pandas as pd

# Load final dataset
df = pd.read_csv("../dataset/final_output.csv")

# Create SQLite database
conn = sqlite3.connect("darkpattern.db")

# Store data in database
df.to_sql(
    "amazon_products",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()
conn.close()

print("✅ Database created successfully!")