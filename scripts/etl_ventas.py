import pandas as pd
import random
from pathlib import Path

SALES_INPUT_FILE = Path(__file__).parent.parent / 'data' / 'sales_data_sample.csv'
CUSTOMERS_FILE = Path(__file__).parent.parent / 'data' / 'clientes.csv'
PRODUCTS_FILE = Path(__file__).parent.parent / 'data' / 'productos.csv'
CLEAN_SALES_OUTPUT = Path(__file__).parent.parent / 'data' / 'ventas_limpias.csv'

COUNTRY_NORMALIZATION = {
    'USA': 'United States',
    'UK': 'United Kingdom',
}


def normalize_country(country):
    if not isinstance(country, str):
        return ''
    return COUNTRY_NORMALIZATION.get(country.strip(), country.strip())


def load_sales():
    df = pd.read_csv(SALES_INPUT_FILE, encoding='latin1')
    df = df[['ORDERNUMBER', 'ORDERDATE', 'PRODUCTCODE', 'QUANTITYORDERED', 'PRICEEACH', 'SALES', 'COUNTRY', 'PRODUCTLINE', 'DEALSIZE']].copy()
    df.columns = ['order_number', 'order_date', 'product_code', 'quantity_ordered', 'unit_price', 'sales', 'country', 'product_line', 'deal_size']
    df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%Y %H:%M', errors='coerce')
    df['country'] = df['country'].apply(normalize_country)
    return df


def load_product_map():
    if PRODUCTS_FILE.exists():
        df_products = pd.read_csv(PRODUCTS_FILE, encoding='utf-8')
        return dict(zip(df_products['producto_nombre'], df_products['producto_id']))
    return {}


def load_customers():
    if CUSTOMERS_FILE.exists():
        return pd.read_csv(CUSTOMERS_FILE, encoding='utf-8')
    return None


def assign_customer_id(df, customers):
    if customers is None or customers.empty:
        df['customer_id'] = (df.index % 100) + 1
        return df

    customers['country_norm'] = customers['pais'].astype(str).str.strip().str.upper()
    df['country_norm'] = df['country'].astype(str).str.strip().str.upper()
    random.seed(42)
    customer_groups = customers.groupby('country_norm')['cliente_id'].apply(list).to_dict()
    default_ids = list(customers['cliente_id'])

    customer_ids = []
    for idx, row in df.iterrows():
        country_key = row['country_norm']
        options = customer_groups.get(country_key, default_ids)
        customer_ids.append(options[idx % len(options)])

    df['customer_id'] = customer_ids
    df = df.drop(columns=['country_norm'])
    return df


def enrich_product_id(df, product_map):
    if product_map:
        df['product_id'] = df['product_code'].map(product_map)
        missing = df['product_id'].isna()
        if missing.any():
            df.loc[missing, 'product_id'] = pd.factorize(df.loc[missing, 'product_code'])[0] + max(product_map.values(), default=0) + 1
    else:
        df['product_id'] = pd.factorize(df['product_code'])[0] + 1
    df['product_id'] = df['product_id'].astype(int)
    return df


def main():
    df = load_sales()
    product_map = load_product_map()
    df = enrich_product_id(df, product_map)
    customers = load_customers()
    df = assign_customer_id(df, customers)

    CLEAN_SALES_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_SALES_OUTPUT, index=False, encoding='utf-8')
    print('Clean sales saved to', CLEAN_SALES_OUTPUT)


if __name__ == '__main__':
    main()
