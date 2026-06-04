import streamlit as sl

home = sl.Page(
    "pages/home.py",
    title="Home"
)

upload = sl.Page(
    "pages/upload_page.py",
    title="Upload"
)

importing = sl.Page(
    "pages/import_data.py",
    title="Importação"
)

data_view = sl.Page(
    "pages/raw_data_view.py",
    title="Visualização"
)

analysis = sl.Page(
    "pages/analysis_page.py",
    title="Análises"
)

pg = sl.navigation(
    {
        "Home": [home],
        "Processamento": [upload, importing],
        "Dados": [data_view],
        "Análises": [analysis]
    }
)

pg.run()