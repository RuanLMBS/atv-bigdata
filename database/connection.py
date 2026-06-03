import streamlit as sl
from sqlalchemy import create_engine
from config.settings import DATABASE_URL

def get_engine():
    try:
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        return engine
    except Exception as e:
        sl.error(f"Erro na conexão com o db! {e}")
        return None