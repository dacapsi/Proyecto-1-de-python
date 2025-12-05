import pandas as pd
import json

# Ruta del archivo de Kaggle
ruta_csv = "C:/Users/Naleska/Documents/globalmarket/datos/ventas.csv"

df = pd.read_csv(ruta_csv)

# Nos quedamos solo con columnas útiles del producto
productos = df[[
    "product_id", 
    "product_name", 
    "category", 
    "discounted_price", 
    "actual_price", 
    "discount_percentage", 
    "rating", 
    "rating_count",
    "about_product",
    "img_link",
    "product_link"
]].drop_duplicates(subset=["product_id"])

# Convertimos a diccionarios
lista_productos = productos.to_dict(orient="records")

# Convertimos a JSON y guardamos
with open("C:/Users/Naleska/Documents/globalmarket/datos/productos.json", "w", encoding="utf-8") as f:
    json.dump(lista_productos, f, indent=4, ensure_ascii=False)

print("Productos generados:", len(lista_productos))