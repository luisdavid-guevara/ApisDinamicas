# Proyecto APP

Este directorio contiene el código fuente del proyecto. A continuación se describen los elementos principales:

## `models`

Este directorio contiene archivos de modelos que representan las tablas de la base de datos. Cada archivo en este directorio define la estructura de una tabla específica en la base de datos.

## `routes`

En este directorio, encontrarás el archivo `api.py` que se encarga de crear rutas dinámicas para las APIs. Estas rutas están relacionadas con las operaciones CRUD para los modelos definidos en la carpeta `models`.

## `utils`

El directorio `utils` incluye el archivo `dynamic_routes.py`, que se utiliza para extraer datos de una tabla y generar rutas dinámicas basadas en esos datos.

## Archivos Principales

- **`BaseApi.py`**: Contiene la base para la creación de rutas dinámicas y la implementación de las operaciones CRUD asociadas.
- **`config.py`**: Almacena la información necesaria para conectarse a la base de datos.
- **`one.py`**: Creado para evitar importaciones circulares en el código y facilitar la organización del proyecto.
- **`run.py`**: Punto de entrada principal para ejecutar el proyecto. Orquesta y ejecuta todas las APIs del sistema.

## Instrucciones de Ejecución

Para ejecutar el proyecto, sigue estos pasos:

1. Asegúrate de tener todas las dependencias instaladas.
2. Ejecuta `python run.py` desde la línea de comandos.
