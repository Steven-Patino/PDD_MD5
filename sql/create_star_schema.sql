-- Esquema estrella para PostgreSQL

CREATE TABLE dim_producto (
    producto_id SERIAL PRIMARY KEY,
    producto_nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(100)
);

CREATE TABLE dim_cliente (
    cliente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    ciudad VARCHAR(100),
    pais VARCHAR(100)
);

CREATE TABLE dim_region (
    region_id SERIAL PRIMARY KEY,
    pais VARCHAR(100) NOT NULL UNIQUE,
    region VARCHAR(100),
    subregion VARCHAR(100),
    continente VARCHAR(100)
);

CREATE TABLE fact_ventas (
    venta_id SERIAL PRIMARY KEY,
    numero_orden INTEGER,
    fecha_orden DATE,
    producto_id INTEGER REFERENCES dim_producto(producto_id),
    cliente_id INTEGER REFERENCES dim_cliente(cliente_id),
    pais VARCHAR(100),
    cantidad_pedida INTEGER,
    precio_unitario NUMERIC(12,2),
    ventas NUMERIC(14,2),
    anio INTEGER,
    mes INTEGER,
    tamano_venta VARCHAR(50),
    FOREIGN KEY (pais) REFERENCES dim_region(pais)
);
