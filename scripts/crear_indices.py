import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["ProyectoGlobal"]

# productos
db.productos.create_index([("product_id", 1)], unique=True, name="product_id_1")
db.productos.create_index([("category", 1)], name="category_1")
db.productos.create_index([("rating", -1)], name="rating_-1")
db.productos.create_index([("category", 1), ("rating", -1)], name="category_1_rating_-1")

# ventas
db.ventas.create_index([("rating", -1)], name="rating_-1")

print("Índices creados (o ya existentes).")

print(db.productos.index_information())