import sqlite3
import pandas as pd

conn = sqlite3.connect("darkpattern.db")

# Query 1 - Top 5 Highest Risk Products
query = """
SELECT product_name,
       DarkPatternScore,
       RiskLevel
FROM amazon_products
ORDER BY DarkPatternScore DESC
LIMIT 5;
"""

df = pd.read_sql(query, conn)

print("Top 5 Highest Risk Products")
print(df)

query = """
SELECT MainCategory,
       ROUND(AVG(rating),2) AS AverageRating
FROM amazon_products
GROUP BY MainCategory;
"""

df = pd.read_sql(query, conn)

print("\nAverage Rating by Category")
print(df)

query = """
SELECT RiskLevel,
       COUNT(*) AS Products
FROM amazon_products
GROUP BY RiskLevel;
"""

df = pd.read_sql(query, conn)

print("\nRisk Distribution")
print(df)

query = """
SELECT product_name,
       discount_percentage
FROM amazon_products
ORDER BY discount_percentage DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)

print("\nHighest Discount Products")
print(df)

conn.close()