# Event Management System

A complete Django + SQLite event management website based on the supplied requirements.

## Features

### User Side
- User registration and login
- Browse upcoming events
- Search and filter events
- Event details page
- Register/book an event
- View my bookings
- Cancel booking
- User profile management
- Change password

### Admin Side
- Staff/admin login
- Dashboard with total events, users and bookings
- Add, edit and delete events
- Manage event categories
- View all bookings
- Approve/reject registrations
- Manage users
- Django admin panel

## Quick Start

### Windows
Double-click `run.bat`.

Or open a terminal in this folder:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Open:
- Website: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/django-admin/

### Demo Accounts

Admin:
- Username: `admin`
- Password: `admin123`

User:
- Username: `demo`
- Password: `demo123`

Change these passwords before using the project publicly.

## Database

SQLite is used by default. The database file is created as `db.sqlite3` after migrations.

## Project Structure

```text
event_management_system/
├── event_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── events/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── management/commands/seed_demo.py
├── templates/
│   ├── base.html
│   ├── registration/
│   ├── events/
│   └── adminpanel/
├── static/css/style.css
├── manage.py
└── requirements.txt
```
