from sqlalchemy import create_engine
import pandas as pd
import os

# Connect to DB
engine = create_engine("postgresql://senthilkumarshreeyasen@localhost:5432/fleetdb")


def run_sql_query(sql: str):
    try:
        df = pd.read_sql_query(sql, con=engine)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

