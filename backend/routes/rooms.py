from flask import Blueprint, jsonify
from pymongo import MongoClient

rooms_bp = Blueprint("rooms", __name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.hotel_booking
rooms = db.rooms

@rooms_bp.route("/rooms", methods=["GET"])
def get_rooms():
    room_list = []
    for room in rooms.find({"available": True}):
        room["_id"] = str(room["_id"])  # convert ObjectId to string
        room_list.append(room)
    return jsonify(room_list)
