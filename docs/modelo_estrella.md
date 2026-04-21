# Modelo en Estrella

Este proyecto usa un modelo de datos en estrella con una tabla de hechos y dimensiones.

## Dimensiones

- `dim_cliente`
  - `cliente_id`
  - `nombre`
  - `ciudad`
  - `pais`

- `dim_producto`
  - `producto_id`
  - `producto_nombre`
  - `categoria`

- `dim_region`
  - `region_id`
  - `pais`
  - `region`
  - `subregion`
  - `continente`

## Tabla de hechos

- `fact_ventas`
  - `venta_id`
  - `order_number`
  - `order_date`
  - `producto_id`
  - `cliente_id`
  - `pais`
  - `quantity_ordered`
  - `price_each`
  - `sales`
  - `year`
  - `month`
  - `deal_size`

## Relaciones

- `fact_ventas.producto_id` → `dim_producto.producto_id`
- `fact_ventas.cliente_id` → `dim_cliente.cliente_id`
- `fact_ventas.pais` → `dim_region.pais`

## Notas

- Los clientes se construyen desde la API `https://randomuser.me/api/`.
- La dimensión de regiones se construye con `https://restcountries.com/v3.1/all`.
- El producto se deriva del código original `PRODUCTCODE` y se transforma en `producto_id`.
