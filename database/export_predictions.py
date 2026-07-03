from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

df = pd.read_sql("SELECT * FROM predictions", engine)

df.to_csv("database/predictions.csv", index=False)

print("✅ predictions.csv created from Supabase")