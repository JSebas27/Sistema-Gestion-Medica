from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["clinica"]
coleccion = db["info_paciente"]