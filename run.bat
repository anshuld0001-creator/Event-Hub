@echo off
title Event Management System
echo =========================================
echo   Event Management System - Django
echo =========================================
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)
call venv\Scripts\activate
echo Installing dependencies...
python -m pip install -r requirements.txt
echo Applying database migrations...
python manage.py migrate
echo Creating demo data if needed...
python manage.py seed_demo
echo.
echo Starting server at http://127.0.0.1:8000/
echo Press CTRL+C to stop the server.
python manage.py runserver
pause
