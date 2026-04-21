from pathlib import Path

from scripts import etl_clientes, etl_productos, etl_regiones, etl_ventas, etl_to_db


def run_pipeline():
    print('Starting ETL pipeline')
    etl_clientes.main()
    etl_productos.main()
    etl_regiones.main()
    etl_ventas.main()
    etl_to_db.main()
    print('ETL pipeline and DB load completed')


if __name__ == '__main__':
    run_pipeline()
