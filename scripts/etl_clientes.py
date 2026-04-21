import pandas as pd
import requests
from pathlib import Path

CUSTOMERS_OUTPUT = Path(__file__).parent.parent / 'data' / 'clientes.csv'
CUSTOMERS_URL = 'https://randomuser.me/api/?results=100'


def fetch_customers():
    response = requests.get(CUSTOMERS_URL)
    response.raise_for_status()
    items = response.json().get('results', [])
    rows = []

    for idx, item in enumerate(items, start=1):
        full_name = f"{item['name']['first'].strip()} {item['name']['last'].strip()}"
        rows.append({
            'cliente_id': idx,
            'nombre': full_name,
            'ciudad': item['location']['city'].strip(),
            'pais': item['location']['country'].strip(),
        })

    return pd.DataFrame(rows)


def main():
    CUSTOMERS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df_customers = fetch_customers()
    df_customers.to_csv(CUSTOMERS_OUTPUT, index=False, encoding='utf-8')
    print('Customers saved to', CUSTOMERS_OUTPUT)


if __name__ == '__main__':
    main()
