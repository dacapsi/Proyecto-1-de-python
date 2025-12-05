import os
from pymongo import MongoClient
from dotenv import load_dotenv
import pprint

load_dotenv()

cliente = MongoClient(os.getenv("MONGODB_URI"))
bd = cliente["ProyectoGlobal"]

pp = pprint.PrettyPrinter(indent=4)

print("\n=== PRUEBAS DE RENDIMIENTO CON EXPLAIN() ===\n")

# 1. Buscar productos por categoría
print("\n1) EXPLAIN - Buscar productos por categoría:\n")

exp1 = bd.productos.find(
    {"category": "electronics"}
).explain()

pp.pprint(exp1)


# 2. Buscar productos por product_id
print("\n2) EXPLAIN - Buscar producto por product_id:\n")

exp2 = bd.productos.find(
    {"product_id": 100}
).explain()

pp.pprint(exp2)


# 3. Buscar ventas/reviews por rating >= 4
print("\n3) EXPLAIN - Buscar reviews con rating >= 4:\n")

exp3 = bd.ventas.find(
    {"rating": {"$gte": 4}}
).explain()

pp.pprint(exp3)


# 4. Agrupación con índice
pipeline = [
    {"$group": {"_id": "$product_id", "reviews": {"$sum": 1}}}
]

exp4 = bd.command(
    "aggregate",
    "ventas",
    pipeline=pipeline,
    explain=True,
    cursor={}
)

print("\n4) EXPLAIN - Agrupación por product_id:\n")
print(exp4)