from database.queries import insert_data

def process_and_insert(df, mapping, table_name):
    columns_to_keep = list(mapping.values())
    df_import = df[columns_to_keep].copy()

    inverse_mapping = {
        v: k for k,
        v in mapping.items()
    }

    df_import.rename(columns = inverse_mapping, inplace=True)

    insert_data(df_import, table_name)

    return len(df_import)
