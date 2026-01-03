import jwt
import datetime
import os
from database import users

SECRET = os.getenv("JWT_SECRET")

def create_user(user):
    if not users.find_one({"telegram_id": user["telegram_id"]}):
        users.insert_one({
            "telegram_id": user["telegram_id"],
            "name": user["name"],
            "points": 0,
            "created_at": datetime.datetime.utcnow()
        })

def generate_token(telegram_id):
    payload = {
        "telegram_id": telegram_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verify_token(token):
    return jwt.decode(token, SECRET, algorithms=["HS256"])
