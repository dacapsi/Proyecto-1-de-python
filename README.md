# GlobalMarket Analisis & Busqueda

Proyecto de Sistema de Bases de Datos Documentales (MongoDB Atlas)  
UNEG — Ingeniería Informática  
Asignatura: Bases de Datos II — Profa. Clinia Cordero  
Semestre: 2025-II


# Descripción General

GlobalMarket Analytics es un proyecto que migra los datos de un e-commerce hacia una base de datos documental en MongoDB Atlas, incorporando:

- Modelado documental con embedding y referencing
- Validaciones JSON Schema
- Pipelines avanzados de agregación
- Búsqueda usando Atlas Search (Lucene)
- Índices para optimizar el rendimiento
- Pruebas con Explain Plan
- Dashboard (opcional) en MongoDB Charts

El sistema maneja productos y ventas, así como reseñas y análisis de comportamiento.


# Estructura del Proyecto

GlobalMarket/
│
├── datos/
│   ├── productos.json
│   ├── resenas.json
│   └── ventas.csv
│
├── scripts/
│   ├── cargar_datos.py
│   ├── consultas_agregacion.py
│   ├── crear_indices.py
│   ├── generar_productos.py
│   ├── prueba_conexion.py
│   └── pruebas_explain.py
│
├── validadores/
│   ├── validation_productos.json
│   └── validation_ventas.json
│
├── .env.template      → Archivo que el usuario debe copiar
├── .gitignore         → Archivo que impide subir .env real
├── README.md
└── requisitos.txt


#  Configuración del Entorno

## 1 Instalar dependencias

pip install pymongo python-dotenv pandas


#  Ingesta de Datos

Importar productos y ventas a MongoDB:

python scripts/cargar_datos.py


#  Ejecución de Aggregation Pipelines

python scripts/consultas_agregacion.py
Incluye:
- Conteo de productos por categoría  
- Top productos por rating  
- Promedio de precios  
- Total de reviews  
- Agregaciones avanzadas (ventas por mes, bucketing, top productos)


#  Validadores (JSON Schema)

Los archivos en validadores/ contienen:

- productos_validador.json
- ventas_validador.json

Puedes aplicarlos desde MongoDB Atlas → Collections → Validation  
o ejecutando tu script de validación.

#  Consultas Básicas
1. Buscar productos por categoría
2. Top 10 productos mejor valorados
3. Precio promedio por categoria
4. Rating promedio por categoria
5. top productos con mas review
6. contento total de ventas

#  Consultas Avanzadas (Aggregation Framework)
1. Total de ventas por categoría y por mes
Usando: $match, $group, $project

2. Top productos con mejor rating y más de 50 reseñas
Usando: $match, $group, $sort, $limit
3. Bucket de precios
Usando $bucketAuto#


#  Atlas Search (Fuzzy Search)

Índice definido en:productos_search_index
Tipo: search
Modo: fuzzy para búsqueda aproximada estilo Amazon

Pipeline:
{
  index: "search_index_productos",
  text: {
    query: "<texto>",
    path: ["product_name", "about_product"],
    fuzzy: { "maxEdits": 2 }
  }
}

# Índices y Rendimiento

Ejecutar:

python scripts/crear_indices.py
Luego comparar en Atlas el Explain Plan antes/después de los índices.


#  Dashboard (opcional)

Opcionalmente, se pueden crear gráficos en MongoDB Charts:

- Ventas por categoría y mes  
- Top productos por rating  
- Distribución por rangos de precios  


# Integrantes del Proyecto

- Carlos Martinez
- Naleska Carrera 
- Genesis Moya

