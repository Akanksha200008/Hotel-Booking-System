from flask import Flask
from flask_cors import CORS
from routes.auth import auth  # make sure this file exists
from routes.rooms import rooms_bp 
from routes.booking import booking_bp
from routes.admin import admin_bp
from routes.auth import auth

app = Flask(__name__)
CORS(app)

# Register the authentication blueprint
app.register_blueprint(auth)
app.register_blueprint(rooms_bp)
app.register_blueprint(booking_bp)
app.register_blueprint(admin_bp)


@app.route("/")
def home():
    return {"message": "Hotel Booking API is running!"}

if __name__ == "__main__":
    app.run(debug=True)
