import streamlit as sl
from database.queries import search_columns 
from services.data_process import process_and_insert

sl.title("Mapeamento e Importação dos Dados")

if "normalized_file" not in sl.session_state:
    sl.warning("Nenhum arquivo .CSV encontrado! Faça upload na página correspondente")
    if sl.button("Página de Upload"):
        sl.switch_page("pages/upload_page.py")
    sl.stop()

df = sl.session_state["normalized_file"]
csv_columns = df.columns.tolist()

sl.subheader("Visualização dos dados carregados no CSV")
sl.dataframe(df.head(3))

table = "estatisticas"
table_columns = search_columns(table)

if not table_columns:
    sl.error(f"Não foi possível carregar as colunas da tabela {table}")
    sl.stop()

sl.subheader("Mapeamento de Colunas")
sl.write(f"Associe as colunas do CSV com as colunas que estão na tabela, para inserir os dados no Banco")

mapping = {}

with sl.form("form_mapeamento"):
    select_options = ["--Ignorar--"] +  csv_columns

    for col_db in table_columns:
        index = 0
        if col_db in csv_columns:
            index = select_options.index(col_db)

        mapping[col_db] = sl.selectbox(f"Coluna no Banco: {col_db}", options=select_options, index=index)
    
    save_btn = sl.form_submit_button("Confirmar e Inserir no Banco")

if save_btn:
    final_mapping = {
        k: v for k,
        v in mapping.items() if v!= "--Ignorar--"
    }

    if not final_mapping:
        sl.error("Nenhuma coluna mapeada para importação!")
        sl.stop()

    try:
        inserted_lines = process_and_insert(df, final_mapping, table)
        sl.success(f"Sucesso! Inseridas {inserted_lines} linhas na tabela {table}")

    except Exception as e:
        sl.error(f"Erro ao inserir dados na tabela! {e}")
