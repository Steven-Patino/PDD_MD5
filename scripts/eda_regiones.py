import pandas as pd
import requests

url = 'https://restcountries.com/v3.1/all?fields=name,cca2,region,subregion,population,area,continents'

try:
    response = requests.get(url)
    response.raise_for_status()

    datos = response.json()
    df = pd.DataFrame(datos)

    print("--- Analisis Exploratorio de Datos (EDA) ---")
    print("\nShape del dataset:")
    print(df.shape)

    print("\nTipos de dato por columna:")
    print(df.dtypes.to_string())

    print("\nPorcentaje de nulos por columna:")
    null_pct = (df.isna().mean() * 100).sort_values(ascending=False).round(2)
    print(null_pct.to_string())

    print("\nObservamos si existen duplicados en las columnas:")
    print(f"{'Columna':<25} | {'¿Tiene duplicados?':<25} | {'Cantidad de duplicados'}")
    print("-" * 65)
        
    for columna in df.columns:
        cantidad = df[columna].duplicated().sum()
        tiene_duplicados = "Sí" if cantidad > 0 else "No"           
        print(f"{columna:<25} | {tiene_duplicados:<25} | {cantidad}")

except Exception as e:
    print(f"Ocurrió un error: {e}")


print(df['continents'][7])