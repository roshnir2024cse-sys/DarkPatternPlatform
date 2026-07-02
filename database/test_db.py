import sqlite3
import pandas as pd

conn = sqlite3.connect("darkpattern.db")

query = """
SELECT
    product_name,
    MainCategory,
    rating,
    discount_percentage,
    DarkPatternScore,
    RiskLevel
FROM amazon_products
ORDER BY DarkPatternScore DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()