import os
import json
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

cliente = MongoClient(os.getenv("MONGODB_URI"))
bd = cliente["ProyectoGlobal"]

# Cargar productos
with open("C:/Users/Naleska/Documents/globalmarket/datos/productos.json", encoding="utf-8") as f:
    productos = json.load(f)

bd.productos.insert_many(productos)
print("Productos insertados:", len(productos))

# Cargar ventas
ventas = pd.read_csv("C:/Users/Naleska/Documents/globalmarket/datos/ventas.csv")
bd.ventas.insert_many(ventas.to_dict(orient="records"))
print("Ventas insertadas:", len(ventas))