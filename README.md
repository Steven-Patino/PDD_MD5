# PDD M5 Project - Steven Patiño

## Description

This project builds an end-to-end analytics solution for the Emausoft use case.
It integrates sales data with external customers and region sources to create a star schema database and support analysis.

## Project structure

- `data/` - original raw files and generated cleaned outputs.
- `Power bi/` - Visual panels that reflect the analysis carried out during the project. 
- `docs/` - documentation for EDA, the star schema model, and integration logic.
- `scripts/` - ETL scripts for sales, customers, products, and regions.
- `sql/` - SQL script to create the star schema tables.
- `.env.example` - example template for PostgreSQL environment variables.
- `main.py` - orchestrates the full ETL pipeline.

## Clone the repository

Clone the project from GitHub with:

```bash
git clone https://github.com/Steven-Patino/PDD_MD5.git
cd PDD_MD5
```

## Dependencies

Install dependencies with UV or pip:

```bash
uv sync
# or
python -m pip install pandas requests numpy python-dotenv sqlalchemy
```

## Environment variables

This project uses a `.env` file to load PostgreSQL connection settings securely. Copy the example file and update the values for your local environment:

```bash
cp .env.example .env
```

Required environment variables:

- `PGHOST` - database host
- `PGPORT` - database port
- `PGUSER` - database user
- `PGPASSWORD` - database password
- `PGDATABASE` - database name

> Do not commit your `.env` file to source control.

## How to run the project

1. Activate the virtual environment:

```bash
source .venv/bin/activate
```

2. Make sure your `.env` file is configured.

3. Run the full ETL pipeline:

```bash
python main.py
```

4. Generated files will be available in `data/`, and PostgreSQL will be populated automatically.

## Database

The PostgreSQL database connection is configured through environment variables in `.env`.

## Individual scripts

- `python scripts/eda_ventas.py` - Sales exploratory data analysis
- `python scripts/eda_clientes.py` - Customers exploratory data analysis
- `python scripts/eda_regiones.py` - Regions exploratory data analysis
- `python scripts/etl_clientes.py` - Generate customer dimension data
- `python scripts/etl_productos.py` - Generate product dimension data
- `python scripts/etl_regiones.py` - Generate region dimension data
- `python scripts/etl_ventas.py` - Clean and transform sales data
- `python scripts/etl_to_db.py` - Load data into PostgreSQL

## Validation

After running the pipeline, verify that data loaded correctly:

```sql
SELECT 'Customers' AS table_name, COUNT(*) AS records FROM dim_cliente
UNION ALL
SELECT 'Products', COUNT(*) FROM dim_producto
UNION ALL
SELECT 'Regions', COUNT(*) FROM dim_region
UNION ALL
SELECT 'Sales', COUNT(*) FROM fact_ventas;
```

## Notes

- The solution uses Python and pandas for cleaning, transformation, and integration.
- The star schema supports efficient sales analysis by customer, product, and region.

