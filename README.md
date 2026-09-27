# Event Hub 🎉

Event Hub is a Django-based event management and booking platform that allows users to discover upcoming events, view event details, register for events, and manage their bookings. It also provides a dedicated staff dashboard for managing events, categories, users, and bookings.

## 📌 About the Project

Event Hub provides a centralized platform for managing and discovering events.

Users can create accounts, browse upcoming events, search and filter events, register for available events, view their bookings, cancel bookings, manage their profiles, and change their passwords.

Staff members can manage events, categories, users, and bookings through a dedicated administration dashboard.

The project demonstrates practical implementation of Django web development, authentication, database management, CRUD operations, event registration workflows, and role-based access control.

## ✨ Features

### 👤 User Features

- User registration
- User login and logout
- Browse upcoming events
- Search events by title, description, or venue
- Filter events by category
- View detailed event information
- Register/book for events
- View personal bookings
- Cancel bookings
- View and update profile
- Change password
- Event availability and remaining seat information

### 🛠️ Staff/Admin Features

- Staff authentication
- Admin dashboard
- View total events
- View total users
- View total bookings
- View pending bookings
- Create events
- Edit events
- Delete events
- Manage event categories
- View and manage bookings
- Approve or reject bookings
- Search and manage users
- Activate/deactivate users
- Django admin panel

## 🎯 Event Management

Each event can contain:

- Event title
- Description
- Category
- Event date
- Event time
- Venue
- Capacity
- Event status
- Booking information

Supported event statuses include:

- Upcoming
- Completed
- Cancelled

## 🎟️ Booking System

Event Hub includes a booking system that allows registered users to reserve seats for upcoming events.

The system automatically tracks:

- Booking status
- Available seats
- Booked seats
- Booking date
- User registration
- Event registration

Booking statuses include:

- Pending
- Approved
- Rejected
- Cancelled

Each user can have only one booking for the same event.

## 🛠️ Technologies Used

- **Python**
- **Django**
- **SQLite**
- **HTML5**
- **CSS3**
- **JavaScript**
- **Django Templates**

## 📂 Project Structure

```text
Event-Hub/
│
├── event_management/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── events/
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       └── seed_demo.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── adminpanel/
│   ├── events/
│   ├── registration/
│   └── base.html
│
├── static/
│   └── css/
│       └── style.css
│
├── manage.py
├── requirements.txt
├── run.bat
├── run.ps1
├── .gitignore
└── README.md





⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/event-hub.git
cd event-hub
2. Create a Virtual Environment
python -m venv venv
3. Activate the Virtual Environment
Windows
venv\Scripts\activate
Linux/macOS
source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Run Database Migrations
python manage.py migrate
6. Add Demo Data

The project includes a demo-data management command:

python manage.py seed_demo
7. Start the Development Server
python manage.py runserver

Open the application in your browser:

http://127.0.0.1:8000/
🔐 Admin Panel

The project includes both a custom staff dashboard and Django's built-in admin panel.

Custom Staff Dashboard
http://127.0.0.1:8000/admin/
Django Admin
http://127.0.0.1:8000/django-admin/

Use a Django staff/superuser account to access administrative features.

👨‍💻 Demo Accounts

The project includes a demo-data command that can create sample users and events.

Run:

python manage.py seed_demo

If demo credentials are provided by the project configuration, use those credentials for testing.

For a public deployment, change all demo passwords and credentials.

🗄️ Database

Event Hub uses SQLite as its default database.

The database is created and updated using Django migrations:

python manage.py makemigrations
python manage.py migrate
🔒 Security

Before deploying this project publicly:

Change the Django SECRET_KEY
Set DEBUG = False
Configure ALLOWED_HOSTS
Use environment variables for sensitive configuration
Change demo account passwords
Use a production-ready database
Configure secure static and media file handling
🚀 Future Improvements

Possible future enhancements include:

Online payment integration
Email booking confirmations
Event reminder notifications
Event image uploads
Advanced event filtering
Calendar integration
QR-code based event tickets
Ticket generation
Event organizer accounts
Analytics dashboard
Online ticket verification
REST API integration
Deployment with PostgreSQL
Cloud hosting and storage
🎯 Project Objective

The main objective of Event Hub is to provide a simple and efficient digital platform for event discovery, registration, and management.

The application brings event browsing, booking, user management, and administrative event management together in one platform.

📄 License

This project is developed for educational and portfolio purposes.

You are free to use and modify the project for learning and personal development.

👨‍💻 Developer

Anshul Dubey
