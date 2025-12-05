import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

cliente = MongoClient(os.getenv("MONGODB_URI"))
bd = cliente["ProyectoGlobal"]


# Validador para la colección PRODUCTOS

validador_productos = {
    "bsonType": "object",
    "required": ["product_id", "product_name", "category"],
    "properties": {
        "product_id": {"bsonType": "int"},
        "product_name": {"bsonType": "string"},
        "category": {"bsonType": "string"},
        "discounted_price": {"bsonType": ["double", "int", "null"]},
        "actual_price": {"bsonType": ["double", "int", "null"]},
        "discount_percentage": {"bsonType": ["double", "string", "null"]},
        "rating": {"bsonType": ["double", "int", "null"]},
        "rating_count": {"bsonType": ["int", "null"]},
        "about_product": {"bsonType": ["string", "null"]},
        "img_link": {"bsonType": ["string", "null"]},
        "product_link": {"bsonType": ["string", "null"]}
    }
}

bd.command({
    "collMod": "productos",
    "validator": validador_productos,
    "validationLevel": "strict",
    "validationAction": "error"
})

print("Validador aplicado a la colección PRODUCTOS.")


# Validador para la colección VENTAS

validador_ventas = {
    "bsonType": "object",
    "required": ["product_id", "user_id", "rating"],
    "properties": {
        "product_id": {"bsonType": "int"},
        "user_id": {"bsonType": "string"},
        "rating": {
            "bsonType": ["double", "int"],
            "minimum": 0,
            "maximum": 5
        },
        "review_title": {"bsonType": ["string", "null"]},
        "review_content": {"bsonType": ["string", "null"]},
        "review_id": {"bsonType": ["string", "null"]}
    }
}

bd.command({
    "collMod": "ventas",
    "validator": validador_ventas,
    "validationLevel": "strict",
    "validationAction": "error"
})

print("Validador aplicado a la colección VENTAS.")