import os
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables
load_dotenv()

# Data files
CUSTOMERS_FILE = Path(__file__).parent.parent / 'data' / 'clientes.csv'
PRODUCTS_FILE = Path(__file__).parent.parent / 'data' / 'productos.csv'
REGIONS_FILE = Path(__file__).parent.parent / 'data' / 'regiones.csv'
SALES_FILE = Path(__file__).parent.parent / 'data' / 'ventas_limpias.csv'

# SQL to create tables
SQL_CREATE_TABLES = """
-- Star schema for PostgreSQL

CREATE TABLE IF NOT EXISTS dim_producto (
    producto_id SERIAL PRIMARY KEY,
    producto_nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS dim_cliente (
    cliente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    ciudad VARCHAR(100),
    pais VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS dim_region (
    region_id SERIAL PRIMARY KEY,
    pais VARCHAR(100) NOT NULL UNIQUE,
    region VARCHAR(100),
    subregion VARCHAR(100),
    continente VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS fact_ventas (
    venta_id SERIAL PRIMARY KEY,
    numero_orden INTEGER,
    fecha_orden DATE,
    producto_id INTEGER REFERENCES dim_producto(producto_id),
    cliente_id INTEGER REFERENCES dim_cliente(cliente_id),
    pais VARCHAR(100),
    cantidad_pedida INTEGER,
    precio_unitario NUMERIC(12,2),
    ventas NUMERIC(14,2),
    tamano_venta VARCHAR(50),
    FOREIGN KEY (pais) REFERENCES dim_region(pais)
);
"""


def get_connection():
    """Create a PostgreSQL connection using environment variables."""
    host = os.getenv('PGHOST')
    port = os.getenv('PGPORT')
    user = os.getenv('PGUSER')
    password = os.getenv('PGPASSWORD')
    database = os.getenv('PGDATABASE')

    if not all([host, port, user, password, database]):
        raise ValueError("Missing PostgreSQL environment variables.")

    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    return create_engine(url)


def create_tables(engine):
    """Execute SQL to create the tables."""
    with engine.connect() as conn:
        conn.execute(text(SQL_CREATE_TABLES))
        conn.commit()
    print("Tables created successfully.")


def load_data(engine):
    """Load CSV files into the database tables."""
    with engine.connect() as conn:
        # Truncate tables in the correct order (fact first for FK constraints)
        conn.execute(text("TRUNCATE TABLE fact_ventas CASCADE"))
        conn.execute(text("TRUNCATE TABLE dim_cliente CASCADE"))
        conn.execute(text("TRUNCATE TABLE dim_producto CASCADE"))
        conn.execute(text("TRUNCATE TABLE dim_region CASCADE"))
        conn.commit()

    # Load dim_cliente
    if CUSTOMERS_FILE.exists():
        df_customers = pd.read_csv(CUSTOMERS_FILE, encoding='utf-8')
        df_customers.to_sql('dim_cliente', engine, if_exists='append', index=False)
        print("Customers loaded.")

    # Load dim_producto
    if PRODUCTS_FILE.exists():
        df_products = pd.read_csv(PRODUCTS_FILE, encoding='utf-8')
        df_products.to_sql('dim_producto', engine, if_exists='append', index=False)
        print("Products loaded.")

    # Load dim_region
    if REGIONS_FILE.exists():
        df_regions = pd.read_csv(REGIONS_FILE, encoding='utf-8')
        df_regions.to_sql('dim_region', engine, if_exists='append', index=False)
        print("Regions loaded.")

    # Load fact_ventas - only the columns that exist in the table
    if SALES_FILE.exists():
        df_sales = pd.read_csv(SALES_FILE, encoding='utf-8')
        fact_columns = ['numero_orden', 'fecha_orden', 'producto_id', 'cliente_id', 'pais', 'cantidad_pedida', 'precio_unitario', 'ventas', 'tamano_venta']
        df_sales_fact = df_sales[fact_columns].copy()
        df_sales_fact.to_sql('fact_ventas', engine, if_exists='append', index=False)
        print("Sales loaded.")


def main():
    try:
        engine = get_connection()
        create_tables(engine)
        load_data(engine)
        print("Data loaded into the database successfully.")
    except Exception as e:
        print(f"Error loading data: {e}")


if __name__ == '__main__':
    main()
