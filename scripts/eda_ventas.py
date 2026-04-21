import pandas as pd
import requests
from pathlib import Path

archivo_csv = Path(__file__).parent.parent / "data" / "sales_data_sample.csv"
df = pd.read_csv(archivo_csv, encoding='latin1')

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

