# Integración de datos

## Fuentes usadas

- `data/sales_data_sample.csv` → ventas
- `https://randomuser.me/api/?results=100` → clientes
- `https://restcountries.com/v3.1/all` → regiones

## Lógica de integración

1. Se construye un dataset de clientes con `cliente_id`, `nombre`, `ciudad` y `pais`.
2. Se construye un dataset de productos con `producto_id`, `producto_nombre` y `categoria`.
3. Se construye un dataset de regiones con país, región, subregión y continente.
4. Se construye la tabla de hechos de ventas usando `producto_id` y `cliente_id`.
5. La asignación de clientes a ventas es determinista y busca coincidir el país de venta con un cliente del mismo país cuando es posible.

## Archivos generados

- `data/clientes.csv`
- `data/productos.csv`
- `data/regiones.csv`
- `data/ventas_limpias.csv`

## Qué se puede analizar

- Evolución de ventas en el tiempo.
- Ventas por país y región.
- Productos con mayor ingreso.
- Rendimiento por cliente.
- Impacto de la ubicación en el comportamiento de compra.
