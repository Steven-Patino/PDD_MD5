import pandas as pd
import requests
from pathlib import Path

REGIONS_OUTPUT = Path(__file__).parent.parent / 'data' / 'regiones.csv'
REGIONS_URL = 'https://restcountries.com/v3.1/all?fields=name,cca2,region,subregion,continents'

NORMALIZE = {
    'USA': 'United States',
    'UK': 'United Kingdom',
}


def normalize_country_name(country):
    name = country.strip()
    return NORMALIZE.get(name, name)


def fetch_country_data():
    response = requests.get(REGIONS_URL)
    response.raise_for_status()
    return response.json()


def build_region_table(items):
    rows = []
    for item in items:
        name = item.get('name', {}).get('common')
        if not name:
            continue
        rows.append({
            'pais': normalize_country_name(name),
            'region': item.get('region', ''),
            'subregion': item.get('subregion', ''),
            'continente': ', '.join(item.get('continents', []) if item.get('continents') else []),
        })
    return pd.DataFrame(rows)


def main():
    data = fetch_country_data()
    df = build_region_table(data)
    df = df.drop_duplicates(subset=['pais']).reset_index(drop=True)
    REGIONS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(REGIONS_OUTPUT, index=False, encoding='utf-8')
    print('Regions saved to', REGIONS_OUTPUT)


if __name__ == '__main__':
    main()
