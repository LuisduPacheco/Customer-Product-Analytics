from src.transformation import *
from src.cleaning import *
from src.load_preparation import create_tables, save_tables
from src.loading import upload_data, verify_upload

def main():

    BASE_PATH: str = './data/raw/base_de_datos.csv'
    CLIENTES_PATH: str = './data/raw/clientes.csv'
    CLEAN_BASE_PATH = 'data/clean/base_de_datos_clean.csv'
    TABLES_CSV_PATH: str = 'data/tables_csv'

    column_fecha_compra = "Fecha de la compra"
    column_precio_producto = "Precio del producto"
    column_total_orden = "Total de la orden"

    # Se remueven basadas en el Análisis Exploratorio
    columnsToRemove: list[str] = ['Género del cliente', 'Edad del cliente']


    # EXTRACT
    df_base: DataFrame = load_data(BASE_PATH)
    df_clientes: DataFrame = load_data(CLIENTES_PATH)

    # CLEAN
    df_base = remove_empty_cols(columnsToRemove,df_base)
    df_base = clean_strings_cols(df_base)
    print("The data has been cleaned.\n\n")

    # TRANSFORM 
    df_base = convert_object_to_date(df_base, column_fecha_compra)
    df_base = convert_object_to_float(df_base, column_precio_producto)
    df_base = convert_object_to_float(df_base, column_total_orden)

    # En el análisis exploratorio se encontró una columna con un total calculado
    # NOTA: Solo para este caso específico se dejó esa columna con dato calculado, lo mejor es eliminarla. 
    df_base = verify_total(df_base, column_precio_producto, 'Cantidad comprada', column_total_orden)
    save_clean_csv(CLEAN_BASE_PATH, df_base)


    # LOAD
    # Preparar tables CSV
    tables = create_tables(df_base, df_clientes)
    save_tables(tables, TABLES_CSV_PATH)

    # Carga a la base de datos
    upload_data()
    verify_upload()

if __name__ == "__main__":
    main()