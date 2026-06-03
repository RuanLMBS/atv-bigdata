from sqlalchemy import inspect
from database.connection import get_engine

def search_columns(table):
    engine = get_engine()

    insp = inspect(engine)

    columns_info = insp.get_columns(table)

    return [column["name"] for column in columns_info]

def insert_data(df, table_name):
    engine = get_engine()
    df.to_sql(table_name, con=engine, if_exists="append", index=False)
