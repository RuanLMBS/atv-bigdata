import streamlit as sl
from services.data_service import list_table,load_table

sl.title("Visualizar Dados Brutos")

tables = list_table()

selected_table = sl.selectbox("Tabela", tables)

if selected_table:
    data = load_table(selected_table)

    sl.dataframe(data)