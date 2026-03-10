School Grading System API

A backend REST API built using Django and Django REST Framework that manages student exam results and automatically calculates grades based on scores.

This project was developed as a Capstone Project to demonstrate backend development skills including API development, database modeling, and implementing automated grading logic.

Project Overview

The School Grading System API allows administrators to input student exam scores and automatically calculate the student's total score and grade.

Instead of manually calculating grades, the system processes the scores and assigns the correct grade automatically based on predefined grading rules.

Key Features

Add student exam results

Automatically calculate total score

Automatically assign grades

REST API endpoints for managing results

Admin dashboard for managing records

Backend grading logic implemented in Django models

Grading Logic

Grades are calculated automatically based on the student's total score.

Score Range	Grade
80 – 100	A
70 – 79	B
60 – 69	C
50 – 59	D
Below 50	F

Example:

Student scores:

Class Score: 30
Exam Score: 50

The system automatically calculates:

Total: 80
Grade: A

Technologies Used

Python

Django

Django REST Framework

SQLite Database

Git

GitHub

Project Structure

school-grading-system-api

config/
Main project configuration and URL routing

results/
Application that handles student results

results/models.py
Contains the Result model and grading logic

results/serializers.py
Handles conversion between JSON and database objects

results/views.py
Defines API endpoints

results/admin.py
Admin dashboard configuration

manage.py
Django management script

db.sqlite3
SQLite database

Installation and Setup

Clone the repository

git clone https://github.com/joel7pap777/school-grading-system-api.git

Navigate to the project directory

cd school-grading-system-api

Create a virtual environment

python -m venv venv

Activate the virtual environment

Windows:

venv\Scripts\activate

Install dependencies

pip install django djangorestframework

Apply migrations

python manage.py migrate

Create an admin user

python manage.py createsuperuser

Run the development server

python manage.py runserver

The application will be available at:

http://127.0.0.1:8000/

API Endpoints
Endpoint	Description
/api/results/	View and create student results
/admin/	Django admin dashboard

Example POST request:

POST /api/results/

{
"student_name": "John Doe",
"class_score": 30,
"exam_score": 50
}

Example response:

{
"student_name": "John Doe",
"class_score": 30,
"exam_score": 50,
"total": 80,
"grade": "A"
}

Admin Dashboard

The system includes a Django admin dashboard that allows administrators to manage student results.

From the admin panel, administrators can:

Add new student results

View automatically calculated totals

View assigned grades

Admin dashboard link:

http://127.0.0.1:8000/admin/
