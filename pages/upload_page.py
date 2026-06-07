import streamlit as sl

from services.normalization import normalize_csv

uploaded_file = sl.file_uploader("Selecione o arquivo .CSV", type=["csv"])


if uploaded_file:
    sl.session_state["uploaded_file"] = uploaded_file
    sl.info("Arquivo carregado com sucesso! Configure as opções de importação abaixo")

    delimiter = sl.selectbox(
    "Qual é o delimitador de colunas?",
    [";",","]
    )

    convert_decimal = sl.checkbox("Converter de vírgula para ponto (Campos Decimais)", value=True)

    trim_spaces = sl.checkbox("Remover espaços extras", value=True)

    if sl.button("Processar"):
        normalized_file,null_report = normalize_csv(uploaded_file, delimiter, trim_spaces=trim_spaces, convert_decimal=convert_decimal)

        sl.session_state["normalized_file"] = normalized_file 
        
        sl.success("Arquivo processado com sucesso!")

        sl.subheader("Validação de Valores Nulos")

        sl.dataframe(
            null_report.reset_index().rename(
                columns={ "index": "Coluna", 0: "Qtd. Nulos"}
            )
        )

        sl.write("Breve visualização dos dados:")
        sl.dataframe(normalized_file.head())