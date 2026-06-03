from sqlalchemy import inspect
import pandas as pd
from database.connection import get_engine

def get_tables():
    engine = get_engine()

    inspector = inspect(engine)

    return inspector.get_table_names()

def search_columns(table):
    engine = get_engine()

    inspector = inspect(engine)

    columns_info = inspector.get_columns(table)

    return [column["name"] for column in columns_info]

def get_table_data(table_name):
    engine = get_engine()

    query = f"SELECT * FROM {table_name}"

    return pd.read_sql(query, engine)

def insert_data(df, table_name):
    engine = get_engine()
    df.to_sql(table_name, con=engine, if_exists="append", index=False)
