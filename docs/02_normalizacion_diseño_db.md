# Normalización y diseño de la Base de Datos

## Estructura inicial

El cliente proporcionó 2 archivos CSV separados. 

**Archivo base_de_datos.csv**: Contiene información mezclada entre productos, ordenes y ventas. Este archivo se compone de 12 columnaas y con 2 de esas columnas vacías.

|ID de la orden|Fecha de la compra|ID del cliente|Género del cliente|Edad del cliente|Categoría del producto|Nombre del producto|Precio del producto|Cantidad comprada|Total de la orden|Método de pago|Región de envío|
|--------------|------------------|--------------|------------------|----------------|----------------------|-------------------|-------------------|-----------------|-----------------|--------------|---------------|
|10001         |2025-04-27        |2687          |                  |                |Pantalones            |Jeans slim         |158,02             |1                |158,02           |Efectivo      |Ciudad         |
|10002         |2025-04-24        |2837          |                  |                |Accesorios            |Bolso de mano      |29,15              |5                |145,75           |Transferencia |Occidente      |
|10003         |2025-05-02        |1328          |                  |                |Zapatos               |Sandalias          |59,83              |3                |179,49           |Efectivo      |Occidente      |


**Archivo clientes:** Contiene información de los clientes, las columnas que faltan en el primer archivo, se encuentran en este segundo archivo. 

|ID del cliente|Género del cliente|Edad del cliente|
|--------------|------------------|----------------|
|1000          |Masculino         |37              |
|1001          |Femenino          |23              |
|1002          |No especifica     |29              |

## Normalización aplicada 

## Primera forma normal

Las tablas deben tener una clave primaria y no deberían tener matrices de valores: 

**Tabla Métodos de pago**

|id_metodo_pago|metodo       |
|--------------|-------------|
|1             |Efectivo     |
|2             |Transferencia|
|3             |Tarjeta      |

## Segunda forma normal 

Primero se debe cumplir con la Primera forma normal.

Segundo, cada dato debe depender de la clave completa de la tabla y no de solo una parte de ella. Si esto no se cumple, esos datos se separan en otra tabla para evitar duplicidad y facilitar el mantenimiento de la información

**Tabla Clientes**

|id_cliente|id_genero_cliente|edad_cliente|
|----------|-----------------|------------|
|2687      |1                |37          |
|2837      |2                |23          |
|1328      |3                |29          |

El género del cliente se separó en otra tabla para evitar duplicidad, cumpliendo esta forma de normalización.

**Tabla Genero del cliente**

|id_genero_cliente|genero       |
|-----------------|-------------|
|1                |Masculino    |
|2                |Femenino     |
|3                |No Especifica|

## Tercera forma normal

La Tercera Forma Normal garantiza que todos los atributos dependan únicamente de la clave primaria y no entre sí. Cuando un atributo depende de otro atributo no clave, se crea una nueva tabla para mantener la información organizada y consistente.

Estas tablas cumplen la Tercera Forma Normal porque todos los atributos dependen únicamente de la clave primaria de su respectiva tabla y no existen dependencias transitivas entre atributos no clave. Además, la información relacionada, como categorías, métodos de pago o regiones de envío, se encuentra separada en tablas independientes para evitar redundancia y mantener la consistencia de los datos.

**Tabla Ordenes**
|id_orden|fecha_compra|id_cliente|id_metodo_pago|id_region_envio|
|--------|------------|----------|--------------|---------------|
|10001   |2025-04-27  |2687      |1             |1              |
|10002   |2025-04-24  |2837      |2             |2              |
|10003   |2025-05-02  |1328      |3             |3              |

**Tabla Productos**

|id_producto|producto          |id_categoria|
|-----------|------------------|------------|
|1          |Camiseta estampada|1           |
|2          |Bolso de mano     |2           |
|3          |Sandalias         |3           |

**Tabla Detalle de Orden**

|id_detalle_orden|id_orden|id_producto|cantidad_comprada|precio_producto|total_orden|
|----------------|--------|-----------|-----------------|---------------|-----------|
|1               |10001   |1          |1                |158,02         |158,02     |
|2               |10002   |2          |5                |29,15          |145,75     |
|3               |10003   |3          |3                |59,83          |179,49     |

**NOTA:**

La columna total_orden es un dato derivado, ya que puede calcularse multiplicando cantidad_comprada por precio_producto. En una normalización estricta podría omitirse para evitar almacenar información redundante. 

Se dejó este campo en la base de datos ya que los precios que están en los archivos originales son variados, para efecto de este proyecto decidí dejarlo, con el pensamiento consiente de que puede omitirse y sería lo mejor para otros proyectos.

## Resumen de tablas generadas

Estas son todas las tablas generadas a partir de la normalización, con el objetivo de diseñar la base de datos. 

**Ordenes**

|id_orden|fecha_compra|id_cliente|id_metodo_pago|id_region_envio|
|--------|------------|----------|--------------|---------------|
|10001   |2025-04-27  |2687      |1             |1              |
|10002   |2025-04-24  |2837      |2             |2              |
|10003   |2025-05-02  |1328      |3             |3              |

**Productos**

|id_producto|producto          |id_categoria|
|-----------|------------------|------------|
|1          |Camiseta estampada|1           |
|2          |Bolso de mano     |2           |
|3          |Sandalias         |3           |

**DetalleOrden**

|id_detalle_orden|id_orden|id_producto|cantidad_comprada|precio_producto|total_orden|
|----------------|--------|-----------|-----------------|---------------|-----------|
|1               |10001   |1          |1                |158,02         |158,02     |
|2               |10002   |2          |5                |29,15          |145,75     |
|3               |10003   |3          |3                |59,83          |179,49     |

**Clientes**

|id_cliente|id_genero_cliente|edad_cliente|
|----------|-----------------|------------|
|2687      |1                |37          |
|2837      |2                |23          |
|1328      |3                |29          |

**Categorias**
|id_categoria|categoria |
|------------|----------|
|1           |Pantalones|
|2           |Accesorios|
|3           |Zapatos   |

**MetodosDePago**

|id_metodo_pago|metodo       |
|--------------|-------------|
|1             |Efectivo     |
|2             |Transferencia|
|3             |Tarjeta      |

**GenerosCliente**

|id_genero_cliente|genero       |
|-----------------|-------------|
|1                |Masculino    |
|2                |Femenino     |
|3                |No Especifica|

**RegionesDeEnvio**

|id_region_envio|region   |
|---------------|---------|
|1              |Ciudad   |
|2              |Occidente|
|3              |Norte    |

## Script SQL

```SQL
CREATE TABLE regiones_envios(
    id_region_envio SMALLINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    region VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE metodos_pago(
    id_metodo_pago SMALLINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    metodo VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE generos_cliente(
    id_genero_cliente SMALLINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    genero VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE categorias(
    id_categoria SMALLINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    categoria VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE clientes(
    id_cliente BIGINT PRIMARY KEY,
    id_genero_cliente SMALLINT NOT NULL,
    edad_cliente SMALLINT NOT NULL,
    FOREIGN KEY (id_genero_cliente)
        REFERENCES generos_cliente(id_genero_cliente)
);

CREATE TABLE productos(
    id_producto INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    id_categoria SMALLINT NOT NULL,
    producto VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_categoria)
        REFERENCES categorias(id_categoria)
);

CREATE TABLE ordenes(
    id_orden BIGINT PRIMARY KEY,
    fecha_compra DATE NOT NULL,
    id_cliente BIGINT NOT NULL,
    id_metodo_pago SMALLINT NOT NULL,
    id_region_envio SMALLINT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_metodo_pago) REFERENCES metodos_pago(id_metodo_pago),
    FOREIGN KEY (id_region_envio) REFERENCES regiones_envios(id_region_envio)
);

CREATE TABLE detalle_orden(
    id_detalle_orden BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    id_orden BIGINT NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad_comprada SMALLINT NOT NULL,
    precio_producto NUMERIC(10,2) NOT NULL,
    total_orden NUMERIC(10,2) NOT NULL,
    FOREIGN KEY (id_orden) REFERENCES ordenes(id_orden) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
    UNIQUE (id_orden, id_producto)
);
```

## Diagrama Entidad Relación

![Diagrama entidad relación](./images/03_DiagramaEntidadRelacion.png)