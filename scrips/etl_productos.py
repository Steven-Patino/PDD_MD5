import pandas as pd
from pathlib import Path

SALES_INPUT_FILE = Path(__file__).parent.parent / 'data' / 'sales_data_sample.csv'
PRODUCTS_OUTPUT = Path(__file__).parent.parent / 'data' / 'productos.csv'

PRODUCT_COLUMNS = ['PRODUCTCODE', 'PRODUCTLINE']


def generate_product_dimension():
    df = pd.read_csv(SALES_INPUT_FILE, encoding='latin1')
    df_products = df[PRODUCT_COLUMNS].drop_duplicates().reset_index(drop=True)
    df_products['producto_id'] = df_products.index + 1
    df_products['producto_nombre'] = df_products['PRODUCTCODE']
    df_products['categoria'] = df_products['PRODUCTLINE']
    df_products = df_products[['producto_id', 'producto_nombre', 'categoria']]
    return df_products


def main():
    PRODUCTS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df_products = generate_product_dimension()
    df_products.to_csv(PRODUCTS_OUTPUT, index=False, encoding='utf-8')
    print('Products saved to', PRODUCTS_OUTPUT)


if __name__ == '__main__':
    main()
