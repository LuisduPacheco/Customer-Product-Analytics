# Análisis de Clientes y Ventas

## Problema a resolver

![Problema](./docs/images/01_ProblemaAnalisis.png)

El cliente tiene los datos en dos archivos de Excel, el primero llamado Base de Datos (contiene información de productos y ventas) el segundo llamado Clientes (contiene información básica de los clientes). 

Estos dos archivos tiene relación entre sí, pero los datos no están bien estructurados y no se sabe si hay datos vacíos, el cliente comenta que quiere tener información sobre sus ventas, productos y clientes para entender como va el negocio y tomar decisiones en base a ellos. 

También el cliente quiere que los datos se organicen de mejor manera, de forma profesional ya que las ventas y los productos van aumentando conforme el paso del tiempo y se ha vuelto dificil mantenerlos en archivos de Excel. 

## Solución Propuesta

![Solución](./docs/images/02_SolucionAnalisis.png)

Como solución, se hará una limpieza y estandarización de los datos, se reemplazarán los archivos de Excel por una Base de Datos relacional, entregando el Diagrama Entidad Relación para que pueda ser implementado posteriormente en un sistema. Además se realizará un Dashboard en Power BI para entender las ventas, los productos y otros indicadores, el Dashboard en Power BI será claro e interactivo para que el cliente pueda ver y entender de forma fácil y pueda tomar las decisiones en base a la información organizada.

La solución se realizará de la siguiente forma:

1. Realizar un Análiss Exploratorio para entender el estado de los datos en los archivos proporcionados.

2. Diseñar una Base de Datos Relacional basada en los datos actuales para poder realizar consultas SQL y poder insertar, actualizar así como mantener los datos y lograr integraciones con otras plataformas de forma sencilla en el futuro. 

3. Crear un Dashboard claro e interactivo en Power BI que ayude a tomar decisiones para el negocio. 

4. Entregar la documentación al cliente, con un análisis y conclusiones que ayuden a entender su información actual.

## Analisis Exploratorio

El análisis detallado se puede encontrar en el siguiente documento: [Análisis Exploratorio Detallado](./docs/01_analisis_exploratorio.md). 

A continuación se muestran los resultados del EDA (Exploration Data Analysis).

### Archivos

- **Archivos Analizados**: base_de_datos.csv, clientes.csv

- **Columnas vacías:** En el archivo base_de_datos.csv se encontraron 2 columnas vacías. "Género del cliente" y "Edad del cliente".

- **Tipos de datos incorrectos:** En el archivo base_de_datos.csv las columnas "Fecha de compra", "Precio del producto" y "Total de la orden" están guardados como cadenas de texto. Deberían estar en tipo Fecha y en tipos Númericos. 

### Integridad de los datos 

En el archivo base_de_datos.csv se tiene el campoc "ID de la orden" como identificador, en el archivo clientes.csv se identificó el campo "ID del cliente", ambos archivos manejan integridad al no haber encontrado registros duplicados. 

### Resumen

Se mostró que el archivo principal tiene 20,000 registros con integriad en clave primaria, existen datos en 2 de las 12 columnas que conteien. Los datos faltantes pertencen al archivo secundario, estos pueden ser relacionados con su clave primaria. 

También se identificaron incongruencias en tipos de datos, esto sugiere una transformación posterior para asegurar la validez de cálculos, consultas y análisis a futuro. 

Hay relación entre los clientes únicos del archivo principal y el total de registros en el archivo secundario clientes.csv, esto confirma la referencia entre ambos conjuntos de datos

# Diseño de la base de Datos

A partir de los archivos proporcionados por el cliente y los resultados del Análisis Exploratorio, se decidió diseñar una base de datos relacional, aplicando normalización para reducir la redundancia y mantener integridad.

El diseño completo de la base de datos se encuentra en el siguiente documento: [Normalización y Diseño detallado](./docs/02_normalizacion_diseño_db.md)

## Normalización

Se refiere a organizar la información en tablas estructuradas. Esto ayuda a repetir datos y reduciendo el espacio ocupado. También ayuda a que los datos sean precisos y coherentes a lo largo del tiempo. 

## Diseño relacional

A partir de la normalización, pasamos de tener un archivo CSV principal con 12 columnas y un archivo secundario con 3 columnas hacia una base de datos relacional con 8 tablas. 

Esto permite consultar información, insertar, eliminar y actualizar datos, brindando un mejor manejo y persistencia optima. 

Diagrama entidad relación: 


![Diagrama ER](./docs/images/03_DiagramaEntidadRelación.png)