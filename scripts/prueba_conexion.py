import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
cliente = MongoClient(os.getenv("MONGODB_URI"))
bd = cliente.get_database()

print("Conexión exitosa a MongoDB Atlas.")
print("Base de datos:", bd.name)