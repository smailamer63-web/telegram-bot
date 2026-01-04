from flask import Flask, request, jsonify
from auth import verify_token
from database import users

app = Flask(__name__)

@app.route("/me")
def me():
    token = request.args.get("8382890875:AAHCA9vHKtwlpRHq45mNVfQ3XATI5m-2lLg")
    data = verify_token(token)

    user = users.find_one(
        {"telegram_id": data["telegram_id"]},
        {"_id": 0}
    )

    return jsonify(user)
