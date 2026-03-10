📘 School Grading System API

A backend REST API built with Django and Django REST Framework that manages student exam results and automatically calculates grades based on scores.

This project was developed as a Capstone Project to demonstrate backend development skills such as API creation, database design, and automated grading logic.

🚀 Features

Add student exam results

Automatically calculate total score

Automatically assign grades

REST API endpoints for managing results

Admin dashboard for managing records

Built using Django REST Framework

The system removes the need to manually calculate grades by automatically computing them based on the scores entered.

🧠 Grading Logic

Grades are calculated automatically using the following rule:

Score	Grade
80 – 100	A
70 – 79	B
60 – 69	C
50 – 59	D
Below 50	F

Example:

Class Score: 30
Exam Score: 50
Total: 80
Grade: A

The system automatically calculates this when the result is saved.

🛠 Tech Stack

Python

Django

Django REST Framework

SQLite Database

Git & GitHub

📂 Project Structure
school-grading-system-api
│
├── config/                # Project settings and main URLs
├── results/               # Results app
│   ├── models.py          # Result model and grading logic
│   ├── views.py           # API views
│   ├── serializers.py     # DRF serializers
│   └── admin.py           # Admin configuration
│
├── manage.py
└── db.sqlite3
