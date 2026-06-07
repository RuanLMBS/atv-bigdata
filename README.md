# Projeto de Big Data - Ruan Brandão e Ubirajara Santana

## Pré-requisitos

Antes de executar o projeto, certifique-se de possuir:

- Python instalado
- PostgreSQL instalado e em execução
- Dependências do projeto instaladas (`pip install -r requirements.txt`)

---

## Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto utilizando como base o arquivo `.env.example`.

```env
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

Preencha os valores de acordo com a configuração do seu banco de dados PostgreSQL.

---

## Criação da Base de Dados

Após configurar o banco de dados e as variáveis de ambiente, crie a tabela utilizada pela aplicação executando a seguinte query SQL:

```sql
CREATE TABLE estatisticas (
    uf VARCHAR(100),
    codigo INTEGER,
    regiao VARCHAR(30),
    area_territorial DOUBLE PRECISION,
    populacao INTEGER,
    densidade_demografica DOUBLE PRECISION,
    matriculas_fundamental INTEGER,
    idh DOUBLE PRECISION,
    receitas DOUBLE PRECISION,
    despesas DOUBLE PRECISION,
    renda_per_capita DOUBLE PRECISION,
    total_veiculos INTEGER
);
```

---

## Instalação das Dependências

Instale as dependências do projeto utilizando:

```bash
pip install -r requirements.txt
```

---

## Execução da Aplicação

Com as variáveis de ambiente configuradas e a tabela criada no banco de dados, execute a aplicação com o comando:

```bash
streamlit run app.py
```

Após a execução, o Streamlit disponibilizará uma URL local para acesso à aplicação.

---

## Utilização

Ao acessar a aplicação, será possível:

- Importar arquivos CSV;
- Realizar processos de normalização dos dados;
- Validar inconsistências e valores nulos;
- Persistir os dados no banco PostgreSQL;
- Visualizar análises e indicadores gerados a partir dos dados importados.

---

## Estrutura Geral do Fluxo

1. Configurar as variáveis de ambiente;
2. Criar a tabela `estatisticas` no PostgreSQL;
3. Instalar as dependências do projeto;
4. Executar a aplicação via Streamlit;
5. Importar e tratar os dados através da interface disponibilizada.