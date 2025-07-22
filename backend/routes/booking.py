from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

booking_bp = Blueprint("booking", __name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.hotel_booking
rooms = db.rooms
bookings = db.bookings

# ✅ Book a Room
@booking_bp.route("/book", methods=["POST"])
def book_room():
    data = request.get_json()
    room_id = data["room_id"]
    guest_name = data["guest_name"]
    checkin = data["checkin"]
    checkout = data["checkout"]

    room = rooms.find_one({"_id": ObjectId(room_id), "available": True})
    if not room:
        return jsonify({"error": "Room not available"}), 400

    # Save booking
    bookings.insert_one({
        "room_id": ObjectId(room_id),
        "room_number": room["room_number"],
        "guest_name": guest_name,
        "checkin": checkin,
        "checkout": checkout
    })

    # Mark room as unavailable
    rooms.update_one({"_id": ObjectId(room_id)}, {"$set": {"available": False}})

    return jsonify({"message": f"Room {room['room_number']} booked successfully!"}), 200

@booking_bp.route("/my-bookings", methods=["GET"])
def get_customer_bookings():
    guest_name = request.args.get("guest")
    if not guest_name:
        return jsonify({"error": "Missing guest name"}), 400
    result = []
    for b in bookings.find({"guest_name": guest_name}):
        b["_id"] = str(b["_id"])
        b["room_id"] = str(b["room_id"])
        result.append(b)
    return jsonify(result)

# ✅ Cancel a Booking
@booking_bp.route("/cancel-booking/<booking_id>", methods=["DELETE"])
def cancel_booking(booking_id):
    booking = bookings.find_one({"_id": ObjectId(booking_id)})

    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    # Mark room available again
    rooms.update_one({"_id": ObjectId(booking["room_id"])}, {"$set": {"available": True}})
    # Delete booking
    bookings.delete_one({"_id": ObjectId(booking_id)})

    return jsonify({"message": f"Booking for Room {booking['room_number']} has been cancelled."}), 200
