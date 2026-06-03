from database.queries import get_tables,get_table_data

def list_table():
    return get_tables()

def load_table(table):
    return get_table_data(table)