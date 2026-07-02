from pandas import DataFrame
import pandas as pd
from pathlib import Path
import os

def load_data(path_csv: str) -> DataFrame:
    try:
        df = pd.read_csv(path_csv)
        return df
    except FileNotFoundError:
        print(f"Error: CSV File was not found. the data has not been loaded.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: Exception when loading the CSV File")


def remove_empty_cols(empty_columns: list, dataframe: DataFrame) -> DataFrame:
    for column in empty_columns:
        if column not in dataframe.columns:
            print(f"Error: Column '{column}' does not exists on DataFrame")
            return pd.DataFrame()

    df_clean = dataframe.drop(columns=empty_columns)
    return df_clean

def clean_strings_cols(dataframe: DataFrame) -> DataFrame:
    new_columns = dataframe.columns.str.strip()
    dataframe.columns = new_columns
    return dataframe

def save_clean_csv(path_clean_csv: str, dataframe: DataFrame) -> None:
    if os.path.exists(path_clean_csv):
        print(f"The file {path_clean_csv} exists. It will be replaced.")

    try: 
        dataframe.to_csv(path_clean_csv,index=False)
        print("The specified data has been transformed")
    except:
        print("Error saving the transformed and cleaned CSV file.")