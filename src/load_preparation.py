from pandas import DataFrame
import os

def create_df_table(df: DataFrame, source_column: str, id_column: str, new_column: str) -> DataFrame:

    table: DataFrame = (
        df[[source_column]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    table[id_column] = table.index + 1

    table = table.rename(columns={source_column:new_column})
    return table


def create_generos_cliente(df_clientes: DataFrame) -> DataFrame:
    generos_cliente: DataFrame = (
        df_clientes[["Género del cliente"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    generos_cliente["id_genero_cliente"] = generos_cliente.index + 1

    generos_cliente = generos_cliente.rename(columns={"Género del cliente":"genero"})
    return generos_cliente


def create_clientes(df_clientes: DataFrame, df_generos_cliente: DataFrame) -> DataFrame:
    clientes: DataFrame = df_clientes[["ID del cliente"]].drop_duplicates()

    clientes = df_clientes.merge(
        df_generos_cliente, left_on="Género del cliente", right_on="genero"
    )

    clientes = clientes.rename(columns={
        "ID del cliente": "id_cliente",
        "Edad del cliente": "edad_cliente"
    })

    clientes = clientes[["id_cliente", "id_genero_cliente", "edad_cliente"]]

    return clientes


def create_productos(df_base: DataFrame, df_categorias: DataFrame) -> DataFrame:
    productos = df_base[["Nombre del producto", "Categoría del producto"]].drop_duplicates()

    productos = productos.merge(
        df_categorias, left_on="Categoría del producto", right_on="categoria"
    )

    productos["id_producto"] = range(1, len(productos) + 1)

    productos = productos.rename(columns={"Nombre del producto": "producto"})

    productos = productos[["id_producto", "producto", "id_categoria"]]
    return productos

def create_ordenes(df_base: DataFrame, df_metodos_pago: DataFrame, df_regiones_envio: DataFrame) -> DataFrame:
    ordenes = df_base.merge(
        df_metodos_pago,
        left_on="Método de pago",
        right_on="metodo"
    )

    ordenes = ordenes.merge(
        df_regiones_envio,
        left_on="Región de envío",
        right_on="region"
    )

    ordenes = ordenes.rename(columns={
        "ID de la orden": "id_orden",
        "Fecha de la compra": "fecha_compra",
        "ID del cliente": "id_cliente"
    })

    ordenes = ordenes[[
        "id_orden",
        "fecha_compra",
        "id_cliente",
        "id_region_envio",
        "id_metodo_pago"
    ]].drop_duplicates()
    return ordenes

def create_detalle_orden(df_base: DataFrame, df_productos: DataFrame) -> DataFrame:
    detalle_orden = df_base.merge(
        df_productos,
        left_on="Nombre del producto",
        right_on="producto"
    )

    detalle_orden = detalle_orden.rename(columns={
        "ID de la orden": "id_orden",
        "Cantidad comprada": "cantidad_comprada",
        "Precio del producto": "precio_producto",
        "Total de la orden": "total_orden"    
    })

    detalle_orden = detalle_orden[[
        "id_orden",
        "id_producto",
        "cantidad_comprada",
        "precio_producto",
        "total_orden"
    ]]

    return detalle_orden

def create_tables(df_base: DataFrame, df_clientes: DataFrame) -> dict[str, DataFrame]:
    generos_cliente = create_df_table(df_clientes, "Género del cliente", "id_genero_cliente", "genero")
    clientes = create_clientes(df_clientes, generos_cliente)
    categorias = create_df_table(df_base, "Categoría del producto", "id_categoria", "categoria")
    metodos_pago = create_df_table(df_base, "Método de pago", "id_metodo_pago", "metodo")
    regiones_envios = create_df_table(df_base, "Región de envío", "id_region_envio", "region")
    productos = create_productos(df_base, categorias)
    ordenes = create_ordenes(df_base, metodos_pago, regiones_envios)
    detalle_orden = create_detalle_orden(df_base, productos)

    return {
        "generos_cliente": generos_cliente,
        "clientes": clientes,
        "categorias": categorias,
        "metodos_pago": metodos_pago,
        "regiones_envios": regiones_envios,
        "productos": productos,
        "ordenes": ordenes,
        "detalle_orden": detalle_orden,
    }

def save_tables(tables: dict[str, DataFrame], output_path: str) -> None:
    if os.path.exists(output_path):
        print(f"The file {output_path} exists. It will be replaced.")

    for name, table in tables.items():
        table.to_csv(
            f"{output_path}/{name}.csv",
            index=False
        )
    
    print("The CSV tables are now ready.")
