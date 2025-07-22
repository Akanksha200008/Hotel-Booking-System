from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

admin_bp = Blueprint("admin", __name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.hotel_booking
rooms = db.rooms
bookings = db.bookings
users = db.users

@admin_bp.route("/admin/bookings", methods=["GET"])
def get_admin_bookings():
    admin_user = request.args.get("admin")
    if not admin_user:
        return jsonify({"error": "Missing admin username"}), 400
    room_ids = [r["_id"] for r in rooms.find({"added_by": admin_user}, {"_id": 1})]
    result = []
    for booking in bookings.find({"room_id": {"$in": room_ids}}):
        booking["_id"] = str(booking["_id"])
        booking["room_id"] = str(booking["room_id"])
        result.append(booking)
    return jsonify(result)

@admin_bp.route("/admin/rooms", methods=["GET"])
def get_admin_rooms():
    admin_user = request.args.get("admin")
    if not admin_user:
        return jsonify({"error": "Missing admin username"}), 400
    result = []
    for room in rooms.find({"added_by": admin_user}):
        room["_id"] = str(room["_id"])
        result.append(room)
    return jsonify(result)

@admin_bp.route("/admin/add-room", methods=["POST"])
def add_room():
    data = request.get_json()
    admin_user = data["admin"]
    user = users.find_one({"username": admin_user})
    hotel_name = user.get("hotel_name", "Unnamed Hotel")

    new_room = {
        "room_number": data["room_number"],
        "type": data["type"],
        "price": int(data["price"]),
        "amenities": data["amenities"],
        "available": True,
        "added_by": admin_user,
        "hotel_name": hotel_name
    }
    rooms.insert_one(new_room)
    return jsonify({"message": "Room added successfully"}), 201

@admin_bp.route("/admin/delete-room/<room_id>", methods=["DELETE"])
def delete_room(room_id):
    result = rooms.delete_one({"_id": ObjectId(room_id)})
    if result.deleted_count == 1:
        return jsonify({"message": "Room deleted successfully"}), 200
    return jsonify({"error": "Room not found"}), 404
