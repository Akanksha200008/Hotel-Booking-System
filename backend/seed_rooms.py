from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.hotel_booking
rooms = db.rooms

# Clear old data
rooms.delete_many({})

# Insert sample rooms
sample_rooms = [
    {
        "room_number": "101",
        "type": "Single",
        "price": 100,
        "amenities": ["WiFi", "TV"],
        "available": True
    },
    {
        "room_number": "102",
        "type": "Double",
        "price": 150,
        "amenities": ["WiFi", "AC", "TV"],
        "available": True
    },
    {
        "room_number": "201",
        "type": "Suite",
        "price": 250,
        "amenities": ["WiFi", "AC", "TV", "Mini Bar"],
        "available": True
    }
    
]

rooms.insert_many(sample_rooms)
print("✅ Sample rooms inserted.")
