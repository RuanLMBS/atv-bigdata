from database.queries import get_tables,get_table_data,get_pop_density,get_avg_idh_pibpc, get_states_above_average_vehicles, get_social_vulnerability

def list_table():
    return get_tables()

def load_table(table):
    return get_table_data(table)

def load_pop_density_insight():
    data = get_pop_density()

    above_average = len(data[data["classificacao"] == "Acima da Média Nacional"])
    below_average = len(data[data["classificacao"] == "Abaixo da Média Nacional"])

    most_dense_state = data.iloc[0]["uf"]

    insight = (
        f"O estado com maior densidade demográfica é {most_dense_state}, sendo portanto o estado mais povoado.\n\n"
        f"Foram identificados {above_average} estados com densidade acima da média nacional e {below_average} estados abaixo da média nacional.\n\n"
        f"Esses estados possuem a tendencia de ter maiores investimentos em infraestrutura urbana, mobilidade, saneamento e serviços públicos devido à elevada concentração populacional."
        f"A urbanização voltada a estas áreas, principalmente {most_dense_state}, podem auxiliar no bem-estar da comunidade e na melhor articulação urbanística e paisagística."
    )

    return data, insight

def load_avg_idh_pibpc_insight():
    data = get_avg_idh_pibpc()

    highest_idh = data.iloc[0]["regiao"]

    maior_renda = (
        data.sort_values( by="renda_per_capita_media", ascending=False).iloc[0]["regiao"]
    )

    very_high_idh_regions = len(data[data["status_idh"] == "Muito Alto"])
    high_idh_regions = len(data[data["status_idh"] == "Alto"])
    medium_idh_regions = len(data[data["status_idh"] == "Medio"])
    low_idh_regions = len(data[data["status_idh"] == "Baixo"])

    insight = (
        f"A região {highest_idh} apresentou o maior IDH médio entre as regiões brasileiras, enquanto o {maior_renda} tem a maior renda per capita média.\n\n"
        f"Foram identificadas {very_high_idh_regions} regiões com IDH Muito Alto, "
        f"{high_idh_regions} com IDH Alto\n\n"
        f"{medium_idh_regions} com IDH Médio\n\n"
        f"{low_idh_regions} com IDH Baixo.\n\n"
        f"Os resultados apresentam a relação diretamente proporcional entre desenvolvimento humano e renda da população, como observado na região {highest_idh}.\n\n"
        f"Regiões com menores indicadores demandam de melhores políticas públicas voltadas à educação, qualificação profissional e geração de renda."
    )

    return data, insight

def load_vehicle_fleet_insight():
    data = get_states_above_average_vehicles()

    above_average = len(
        data[data["classificacao"] == "Acima da Média Nacional"]
    )

    below_average = len(data[data["classificacao"] == "Abaixo da Média Nacional"])

    state_highest_fleet = data.iloc[0]["uf"]

    national_media = data.iloc[0]["media_nacional"]

    insight = (
        f"A média nacional de veículos é de, aprox.: "
        f"{national_media:,.0f}. \n\n"
        f"O estado com maior frota é {state_highest_fleet}.\n\n"
        f"Foram identificados {above_average} estados com frota acima da média nacional e {below_average} abaixo da média.\n\n"
        f"A concentração de frota nos estados acima da média sugerem a necessidade da implantação de boas políticas de urbanização, além de maior intensidade econômica e maiores"
        "demandas por infraestruturas viárias, bem como mobilidade urbana exigente.\n\n"
        f"O investimento em transportes e mobilidade torna-se indispensável nestes locais."
    )

    return data, insight

def load_social_vulnerability_insight():
    data = get_social_vulnerability()

    vulnerables = len(data[data["classificacao"] == "Alta Vulnerabilidade Social"])

    worse_state_metrics = data.iloc[0]["uf"]

    insight = (
        f"Existem {vulnerables} estados classificados com alta vulnerabilidade social.\n\n"
        f"O estado com menor renda per capita dentro deste grupo é: {worse_state_metrics}\n\n." 
        f"A combinação de ambos os dados é essencial para direcionar a criação de políticas públicas educacionais e para setores empregatícios, especialmente no(a) {worse_state_metrics}\n\n" 
        f"Tal dado é essencial para gestores públicos e entidades a direcionarem investimentos a estes estados."
    )

    return data, insight