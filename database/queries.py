from sqlalchemy import inspect, text
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

def get_pop_density():
    query = """
        SELECT uf, regiao, populacao, area_territorial,
            ROUND(populacao / area_territorial, 2) 
            AS densidade_calculada,

            CASE
                WHEN (populacao / area_territorial) > ( SELECT AVG(populacao/area_territorial) FROM estatisticas)
                THEN 'Acima da Média Nacional'
                ELSE 'Abaixo da Média Nacional'
            END AS classificacao

        FROM estatisticas

        ORDER BY densidade_calculada DESC
    """

    engine = get_engine()

    return pd.read_sql(text(query),engine)

def get_avg_idh_pibpc():
    query = """
        SELECT
        regiao,
        ROUND(AVG(idh)::NUMERIC, 3) AS idh_medio,
        ROUND(AVG(renda_per_capita)::NUMERIC, 2) AS renda_per_capita_media,

        CASE
            WHEN AVG(idh) >= 0.800 THEN 'Muito Alto'
            WHEN AVG(idh) >= 0.700 THEN 'Alto'
            WHEN AVG(idh) >= 0.600 THEN 'Medio'
            ELSE 'Baixo'
        END AS status_idh,

        CASE
            WHEN AVG(renda_per_capita) >= 2500 THEN 'Alta Renda'
            WHEN AVG(renda_per_capita) >= 1500 THEN 'Média Renda'
            ELSE 'Baixa Renda'
        END AS status_renda

        FROM estatisticas GROUP BY regiao
        ORDER BY idh_medio DESC;
    """

    engine = get_engine()

    return pd.read_sql(text(query),engine)

def get_states_above_average_vehicles():
    query = """
        SELECT uf, total_veiculos,
            ( SELECT AVG(total_veiculos) FROM estatisticas) AS media_nacional,

            CASE
                WHEN total_veiculos >
                    ( SELECT AVG(total_veiculos) FROM estatisticas)
                THEN 'Acima da Média Nacional'
                ELSE 'Abaixo da Média Nacional'
            END AS classificacao

        FROM estatisticas

        ORDER BY total_veiculos DESC;
    """

    engine = get_engine()

    return pd.read_sql(text(query),engine)

def get_social_vulnerability():
    query = """
        SELECT uf, renda_per_capita, matriculas_fundamental,
        CASE
            WHEN renda_per_capita < 1500
                AND matriculas_fundamental > 200000
            THEN 'Alta Vulnerabilidade Social'
            ELSE 'Fora do Critério'
        END AS classificacao

        FROM estatisticas
        WHERE renda_per_capita < 1500 AND matriculas_fundamental > 200000
        ORDER BY renda_per_capita ASC;
    """

    engine = get_engine()

    return pd.read_sql(text(query),engine)