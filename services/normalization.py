import pandas as pd
from utils.regions import REGIOES

def normalize_csv(file, delimiter, trim_spaces, convert_decimal):
    raw_file = pd.read_csv(file, sep=delimiter, encoding="latin1")

    if trim_spaces:
        raw_file.columns = raw_file.columns.str.strip()
        for column in raw_file.select_dtypes(include=["object","string"]):
            raw_file[column] = raw_file[column].str.strip()

    if convert_decimal:
         for column in raw_file.select_dtypes(include=["object", "string"]).columns:
             raw_file[column] = raw_file[column].str.replace(",",".", regex=False)

    normalized_file = add_region_column(raw_file)

    normalized_file = normalized_file.fillna(0)

    null_report = normalized_file.isnull().sum()
    
    return normalized_file, null_report

def validate_null (file):
    return file.isnull().sum()

def add_region_column(file):
    file["regiao"] = file["UF [-]"].map(REGIOES)

    return file