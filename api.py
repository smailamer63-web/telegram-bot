from flask import Flask, request, jsonify
from auth import verify_token
from database import users

app = Flask(__name__)

@app.route("/me")
def me():
    token = request.args.get("token")
    data = verify_token(token)

    user = users.find_one(
        {"telegram_id": data["telegram_id"]},
        {"_id": 0}
    )

    return jsonify(user)
