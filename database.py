from pymongo import MongoClient
import os

MONGO_URL = os.getenv("mongodb+srv://Smailte:<db_password>@cluster0.rz7tbr9.mongodb.net/?appName=Cluster0")

client = MongoClient(MONGO_URL)
db = client.telegram
users = db.users
