# Análsis Exploratorio

Este es un análisis inicial que tiene como objetivo entender la estructura de los archivos CSV proporcionados para la práctica (base_de_datos y clientes). Entender estos archivos incluye conocer los tipos de datos, valores null, valores únicos, número de columnas y filas. Esto ayuda a tomar mejores decisiones para realizar la limpieza de datos.

El código completo puede encontrarse en: https://colab.research.google.com/drive/1vHVS1R9F6u6Jew0t423DIH2raZGkQZUr?usp=sharing

## Información de los archivos

### Archivo base_de_datos.csv

Los resultados muestran que el archivo tiene 20,000 registros.

Se identificó que las columnas “Género del cliente” y “Edad del cliente” presentan 0 valores no nulos y están tipadas como float64, lo cual indica que el archivo principal carece de información del cliente. Esto sugiere que dichos datos deben integrarse desde el archivo clientes.csv mediante la clave ID del cliente.

Existen tipos incorrectos en las columnas“Fecha de la compra, Precio del producto y Total de la orden” ya que están tipados como **object** lo que indica que estos valores están almacenados como texto y deberían estar con tipo **fecha** y **numérico (float64 o int64)** respectivamente para poder realizar consultas y operaciones posteriores de forma correcta.


```Shell
RangeIndex: 20000 entries, 0 to 19999
Data columns (total 12 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   ID de la orden          20000 non-null  int64  
 1   Fecha de la compra      20000 non-null  object 
 2   ID del cliente          20000 non-null  int64  
 3   Género del cliente      0 non-null      float64
 4   Edad del cliente        0 non-null      float64
 5   Categoría del producto  20000 non-null  object 
 6   Nombre del producto     20000 non-null  object 
 7   Precio del producto     20000 non-null  object 
 8   Cantidad comprada       20000 non-null  int64  
 9   Total de la orden       20000 non-null  object 
 10  Método de pago          20000 non-null  object 
 11  Región de envío         20000 non-null  object
dtypes: float64(2), int64(3), object(7)
```

### Archivo clientes.csv

Los resultados muestran que el archivo tiene 1,987 registros.
Hay un total de 3 columnas, de las cuales ninguna contiene valores nulos. Y están correctamente tipados los datos, permitiendo almacenar en texto el **Género del cliente** y en valores numéricos enteros la **Edad del cliente.**


```Shell
RangeIndex: 1987 entries, 0 to 1986
Data columns (total 3 columns):
 #   Column              Non-Null Count  Dtype 
---  ------              --------------  ----- 
 0   ID del cliente      1987 non-null   int64 
 1   Género del cliente  1987 non-null   object
 2   Edad del cliente    1987 non-null   int64 
dtypes: int64(2), object(1)

```

## Detalle de los valores

Una vez conocidos los nombres de las columnas, se analizaron algunas columnas ('ID de la orden', 'ID del cliente', 'Categoría del producto',  'Método de pago', 'Región de envío') para entender el estado actual del archivo.

### Archivo base_de_datos.csv

Se verificó del campo “ID de la orden”, confirmando que no existen registros duplicados, lo cual garantiza integridad en la identificación de cada transacción.


El 'ID del cliente' muestra un conteo de 1,987 valores únicos, esto muestra una relación con el archivo clientes.csv, puede indicar que los clientes del archivo secundario tienen al menos una orden realizada.

La 'Categoría del producto' indica que hay 6 categorías disponibles. Aunque el enunciado menciona 3 categorías (ropa, calzado y accesorios) esto puede servir para el análisis posterior. 
 
La columna 'Método de pago' muestra que hay 5 opciones que luego pueden ayudar a entender si existe una relación entre el valor en las ordenes y el método utilizado. 

La 'Región de envío' indica que el negocio tiene cobertura en 5 localidades a las que pueden llegar los productos.

```Shell
Órdenes únicas: True
Clientes únicos: 1987
Categorías únicas: 6
Métodos de pago únicos: 5Categorías: Método de pago
Tarjeta de crédito    6786
Transferencia         3394
Contra entrega        3374
Tarjeta de débito     3237
Efectivo              3209
Regiones únicas: 5
```