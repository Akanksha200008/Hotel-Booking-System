from flask import Blueprint, request, jsonify
from pymongo import MongoClient
import bcrypt

auth = Blueprint("auth", __name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.hotel_booking
users = db.users

@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data["email"]
    username = data["username"]
    password = data["password"]
    role = data["role"]
    hotel_name = data.get("hotel_name", "")

    if users.find_one({"email": email}):
        return jsonify({"error": "Email already registered"}), 409

    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    users.insert_one({
        "email": email,
        "username": username,
        "password": hashed_pw,
        "role": role,
        "hotel_name": hotel_name
    })

    return jsonify({"message": "User registered successfully"}), 201

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    user = users.find_one({"email": email})
    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return jsonify({
            "message": "Login successful",
            "username": user["username"],
            "role": user["role"],
            "hotel_name": user.get("hotel_name", "")
        }), 200

    return jsonify({"error": "Invalid credentials"}), 401
