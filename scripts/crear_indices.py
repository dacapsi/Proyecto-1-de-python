import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

cliente = MongoClient(os.getenv("MONGODB_URI"))
bd = cliente["ProyectoGlobal"]

# Índices recomendados para productos
bd.productos.create_index("product_id", unique=True)
bd.productos.create_index("product_name")
bd.productos.create_index("category")

# Índices recomendados para ventas (reseñas)
bd.ventas.create_index("user_id")
bd.ventas.create_index("product_id")
bd.ventas.create_index("rating")

print("Índices creados correctamente.")