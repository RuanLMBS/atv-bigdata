import streamlit as sl

from services.data_service import load_pop_density_insight, load_avg_idh_pibpc_insight, load_vehicle_fleet_insight, load_social_vulnerability_insight

sl.title("Análises e Insights")

tab1, tab2, tab3, tab4 = sl.tabs([
    "Desafio 1",
    "Desafio 2",
    "Desafio 3",
    "Desafio 4"
])

with tab1:
    df, insight = load_pop_density_insight()

    sl.subheader("Densidade Demográfica")

    sl.dataframe(df)

    sl.subheader("Gráfico")

    sl.bar_chart( data=df,  x="uf", y="densidade_calculada")

    sl.subheader("Insights - Densidade Demográfica")

    sl.markdown(insight)

with tab2:

    sl.header("IDH e Renda Per Capita")

    df, insight = load_avg_idh_pibpc_insight()

    sl.subheader("Resultado por Região")

    sl.dataframe(
        df,
        use_container_width=True
    )

    col1, col2 = sl.columns(2)

    with col1:
        sl.write("IDH Médio")
        sl.bar_chart(
            data=df,
            x="regiao",
            y="idh_medio"
        )

    with col2:
        sl.write("Média Renda Per Capita")
        sl.bar_chart(
            data=df,
            x="regiao",
            y="renda_per_capita_media"
        )

    sl.subheader("Insight Automático")

    sl.info(insight)

with tab3:

    sl.header("Frota Veícular Nacional")

    df, insight = load_vehicle_fleet_insight()

    df_above_average = df[df["classificacao"]=="Acima da Média Nacional"]

    sl.subheader("Média de Veículos por Estado")

    sl.dataframe( df, use_container_width=True)

    sl.subheader("Visualização")

    sl.bar_chart(data=df,x="uf",y="total_veiculos")

    sl.subheader("Estados com frota acima da Média Nacional")

    sl.dataframe( df_above_average, use_container_width=True)

    sl.subheader("Visualização")

    sl.bar_chart(data=df_above_average,x="uf",y="total_veiculos")

    sl.subheader("Insight Automático")

    sl.info(insight)

with tab4:

    sl.header("Vulnerabilidade Social")

    df, insight = load_social_vulnerability_insight()

    sl.subheader("Estados com alta Vulnerabilidade Social")

    sl.dataframe( df, use_container_width=True)

    sl.subheader("Gráfico")

    sl.bar_chart(data=df,x="uf",y="renda_per_capita")

    sl.subheader("Insights")

    sl.info(insight)