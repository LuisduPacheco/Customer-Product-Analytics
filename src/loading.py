import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
# Configuración
DATA_PATH = Path("./data/tables_csv")
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Orden de carga (respetando dependencias)
TABLAS_EN_ORDEN = [
    ("generos_cliente.csv", "generos_cliente"),
    ("categorias.csv", "categorias"),
    ("metodos_pago.csv", "metodos_pago"),
    ("regiones_envios.csv", "regiones_envios"),
    ("clientes.csv", "clientes"),  # Depende de generos_cliente
    ("productos.csv", "productos"),  # Depende de categorias
    ("ordenes.csv", "ordenes"),  # Depende de clientes, metodos_pago, regiones
    ("detalle_orden.csv", "detalle_orden"),  # Depende de ordenes, productos
]

def upload_data():
    engine = create_engine(DB_URL)
    
    # Usar begin() para que sea transaccional
    with engine.begin() as conn:
        # Opcional: Limpiar tablas existentes (orden inverso por FK)
        print("Cleaning Existing Tables...")
        conn.execute(text("TRUNCATE TABLE detalle_orden, ordenes, productos, clientes, categorias, metodos_pago, regiones_envios, generos_cliente RESTART IDENTITY CASCADE;"))
        
        # Cargar cada tabla
        for archivo, tabla in TABLAS_EN_ORDEN:
            print(f"Cargando {tabla} desde {archivo}...")
            df = pd.read_csv(DATA_PATH / archivo)
            
            # Insertar
            df.to_sql(tabla, conn, if_exists='append', index=False, method='multi',chunksize=100)
            
        print("All tables have been successfully loaded")

def verify_upload():
    engine = create_engine(DB_URL)
    
    with engine.connect() as conn:
        # Contar registros en cada tabla
        tablas = ['generos_cliente', 'categorias', 'metodos_pago', 'regiones_envios', 
                  'clientes', 'productos', 'ordenes', 'detalle_orden']
        
        print("\n=== LOAD VERIFICATION ===")
        for tabla in tablas:
            resultado = conn.execute(text(f"SELECT COUNT(*) FROM {tabla}")).scalar()
            print(f"{tabla:20s}: {resultado:6d} registros")
