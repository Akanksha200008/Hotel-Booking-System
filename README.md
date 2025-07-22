# Hotel-Booking-System
A role-based web application built for hotel room management and online booking, supporting both Admins and Customers, with secure login, CRUD operations, and real-time data updates.

Project Overview
The Hotel Booking Management System simplifies hotel room management and guest bookings. It enables:
Admins to manage rooms they own (add, edit, delete, view bookings).
Customers to browse, filter, book, and cancel hotel room reservations.
Real-time updates to room availability using a MongoDB backend.

Built as part of the CIS 552: Database Design course (Spring 2025), this project emphasizes the use of modern web technologies and NoSQL database modeling with a user-friendly interface.

User Roles & Features
🔐 Login & Registration
Secure login with password hashing (bcrypt)
Role-based redirection (Admin / Customer)
Role stored in MongoDB with user data

👤 Admin Dashboard
Add, update, delete rooms
View only rooms and bookings added by themselves
Room metadata includes: type, price, amenities, hotel name

🧍 Customer Dashboard
Browse available rooms with filters (price, room type, amenities)
Book rooms with check-in/check-out dates
Cancel bookings, which instantly updates availability

🗃️ Database Design (MongoDB)
Database: hotel_booking
Collections:
users: stores user login details, hashed passwords, roles
rooms: contains room info (price, type, availability, owner)
bookings: tracks customer reservations with date ranges
Data is updated in real-time via embedded MongoDB queries when bookings or cancellations occur.

🛠️ Technologies Used
Frontend:	HTML, CSS, JavaScript, Fetch API
Backend:	Python, Flask, PyMongo, bcrypt
Database:	MongoDB (NoSQL)
Security:	Password encryption using bcrypt

🚀 Workflow
1. User Registration/Login
Users register as either Admin (with hotel name) or Customer.
Secure authentication logic handled in Flask (auth.py).

2. Room Management (Admin)
Admins add/update/delete rooms.
Room availability and details stored in rooms collection.
Admins can only manage their own rooms (authorization enforced).

3. Room Browsing & Booking (Customer)
Customers browse filtered rooms.
Booking updates bookings and changes room status to available = false.
Cancellations revert availability status.

4. Real-time Sync
Booked rooms are hidden from available listings.
Cancellations reflect immediately in the UI and database.


Admin dashboard:
Room filter feature:
Booking history page:
MongoDB collections:

🔮 Future Enhancements
Multi-hotel support for a single admin
Enhanced user analytics (frequent guest tracking)
Email notifications for bookings and cancellations
Role: System Administrator for DB maintenance
