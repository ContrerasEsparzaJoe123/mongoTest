import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://joec:that1guy2@cluster0-tlgse.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["parcial2"]
collection = db ["dist"]


distancia = 340.89
pop = 32
post = { "Distanncia": str(distancia), "prueba": str(pop) }

collection.insert_one(post)

