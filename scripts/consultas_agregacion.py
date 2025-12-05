import os
from pymongo import MongoClient
from dotenv import load_dotenv
import pprint

load_dotenv()

cliente = MongoClient(os.getenv("MONGODB_URI"))
bd = cliente["ProyectoGlobal"]

pp = pprint.PrettyPrinter(indent=4)

print("=== AGREGACIONES SOBRE PRODUCTOS ===\n")

# 1. Contar cuántos productos hay por categoría
agg1 = bd.productos.aggregate([
    {"$group": {"_id": "$category", "total_productos": {"$sum": 1}}},
    {"$sort": {"total_productos": -1}}
])
print("1) Productos por categoría:")
pp.pprint(list(agg1))
print("\n----------------------------------------\n")

# 2. Top 10 productos con mejor rating
agg2 = bd.productos.aggregate([
    {"$sort": {"rating": -1}},
    {"$limit": 10},
    {"$project": {"_id": 0, "product_name": 1, "rating": 1}}
])
print("2) Top 10 productos mejor valorados:")
pp.pprint(list(agg2))
print("\n----------------------------------------\n")

# 3. Precio promedio por categoría
agg3 = bd.productos.aggregate([
    {"$group": {
        "_id": "$category",
        "precio_promedio": {"$avg": "$actual_price"}
    }},
    {"$sort": {"precio_promedio": -1}}
])
print("3) Precio promedio por categoría:")
pp.pprint(list(agg3))
print("\n----------------------------------------\n")

# 4. Promedio de rating por categoría
agg4 = bd.productos.aggregate([
    {"$group": {
        "_id": "$category",
        "rating_promedio": {"$avg": "$rating"}
    }},
    {"$sort": {"rating_promedio": -1}}
])
print("4) Rating promedio por categoría:")
pp.pprint(list(agg4))
print("\n----------------------------------------\n")


print("=== AGREGACIONES SOBRE VENTAS/REVIEWS ===\n")

# 5. Número de reviews por producto
agg5 = bd.ventas.aggregate([
    {"$group": {
        "_id": "$product_id",
        "total_reviews": {"$sum": 1}
    }},
    {"$sort": {"total_reviews": -1}},
    {"$limit": 10}
])
print("5) Top 10 productos con más reviews:")
pp.pprint(list(agg5))
print("\n----------------------------------------\n")

# 6. Conteo total de ventas/reviews
agg7 = bd.ventas.aggregate([
    {"$count": "total_registros"}
])
print("7) Total de registros en ventas:")
pp.pprint(list(agg7))
print("\n----------------------------------------\n")

print("=== AGREGACIONES AVANZADAS) ===\n")

# 7.Reporte de Ventas 
agg8 = bd.ventas.aggregate([
  {
    "$match": {
      "timestamp": { "$exists": True }
    }
  },
  {
    "$project": {
      "product_id": 1,
      "category": 1,
      "month": { "$month": "$timestamp" },
      "year": { "$year": "$timestamp" }
    }
  },
  {
    "$group": {
      "_id": { "category": "$category", "month": "$month", "year": "$year" },
      "total_ventas": { "$sum": 1 }
    }
  },
  {
    "$sort": { "_id.year": 1, "_id.month": 1 }
  }
])
print("8) Reporte de Ventas por Categoría, Mes y Año:")
pp.pprint(list(agg8))
print("\n----------------------------------------\n")


# 8. Top productos 

agg9 = bd.ventas.aggregate([
  {
    "$group": {
      "_id": "$product_id",
      "promedio_rating": { "$avg": "$rating" },
      "total_reviews": { "$sum": 1 }
    }
  },
  {
    "$match": {
      "total_reviews": { "$gt": 50 } # Filtra los que tienen más de 50 reviews
      }
  },
  {
    "$sort": { "promedio_rating": -1 }
  },
  {
    "$limit": 10
  }
])
print("9) Top 10 Productos con mejor rating promedio (> 50 reviews):")
pp.pprint(list(agg9))
print("\n----------------------------------------\n")


# 9. Bucket Pattern )
agg10 = bd.productos.aggregate([
  {
    "$bucketAuto": {
      "groupBy": "$actual_price",
      "buckets": 3, # Crea 3 rangos (Bajo, Medio, Alto) automáticamente
      "output": {
        "cantidad_productos": { "$sum": 1 },
        "precio_promedio": { "$avg": "$actual_price" }
      }
    }
  }
])
print("10) Bucket Pattern: Productos agrupados por 3 Rangos de Precio (automático):")
pp.pprint(list(agg10))
print("\n----------------------------------------\n")

# Cierra la conexión al cliente
cliente.close()
print("Conexión a MongoDB cerrada.")