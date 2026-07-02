from src.cleaning import load_data
from pandas import DataFrame
import pandas as pd


def convert_object_to_date(df_clean: DataFrame, column_name: str) -> DataFrame:
    if len(df_clean) == 0:
        return df_clean
    
    try:
        df_clean[column_name] = pd.to_datetime(df_clean[column_name], format='%Y-%m-%d')
        return df_clean
    except Exception as e:
        print(f"Error: Exception when converting {column_name} to date")


def convert_object_to_float(df_clean: DataFrame, column_name) -> DataFrame:
    if len(df_clean) == 0:
        print(f"Error convert precio. The DataFrame '{df_clean}' is empty.")
        return df_clean
    try:
        df_clean[column_name] = pd.to_numeric(df_clean[column_name].str.replace(',','.'), errors='coerce')
        return df_clean
    except Exception as e:
        print(f"Error: Exception when converting {column_name} to float")

    
def verify_total(df_clean: DataFrame, col_price: str, col_quantity: str, col_total: str) -> DataFrame:
    df_clean["calculated_total"] = (df_clean[col_price] * df_clean[col_quantity]).round(2)
    errors: DataFrame = df_clean[df_clean["calculated_total"] != df_clean[col_total]]
    
    if len(errors) != 0:
        print(f"The column {col_total} have incosistent values")
        print(errors[[col_price, col_quantity, col_total, "calculated_total"]].head(3))
    else:
        print(f"The column {col_total} doesn't have incosistent values")
    
    df_clean = df_clean.drop(columns="calculated_total")
    return df_clean