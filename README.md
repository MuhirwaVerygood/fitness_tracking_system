# Fitness Tracking System

---

## Table of Contents

- [Fitness Tracking System](#fitness-tracking-system)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Project Structure](#project-structure)
  - [Getting Started](#getting-started)

---

## Project Overview

The **Fitness Tracking System** is a web application that helps users manage and track their fitness goals. Users can log meals, track their exercise routines, and monitor their progress over time. Based on user inputs such as body measurements, diet, and exercise, the system provides personalized recommendations to support healthy living and fitness.

---

## Features

- **User Profile**: Manage user information including height, weight, and fitness goals.
- **Meal Logging**: Track meals with calorie information to monitor daily intake.
- **Exercise Logging**: Record exercises with duration and calories burned.
- **Personalized Recommendations**: Get daily recommendations for meals and exercises.
- **Dashboard and Analytics**: Visualize data on a user-friendly dashboard with charts to track progress over time.

---

## Technologies Used

- **Backend**: Django, PostgreSQL (database)
- **Frontend**: Django templates, HTML, Bootstrap CSS
- **Visualization**: Chart.js for interactive charts and analytics
- **Database Connection**: psycopg2-binary for PostgreSQL

---

## Project Structure

Here’s an overview of the directory structure for the **Fitness Tracking System** project:
.gitignore .idea ├── .gitignore ├── fitness_tracking_system.iml ├── inspectionProfiles │ ├── Project_Default.xml │ └── profiles_settings.xml ├── misc.xml └── modules.xml .vscode └── settings.json README.md activityapp ├── init.py ├── pycache │ ├── init.cpython-311.pyc │ ├── init.cpython-313.pyc │ ├── admin.cpython-311.pyc │ ├── admin.cpython-313.pyc │ ├── apps.cpython-311.pyc │ ├── apps.cpython-313.pyc │ ├── forms.cpython-311.pyc │ ├── forms.cpython-313.pyc │ ├── models.cpython-311.pyc │ ├── models.cpython-313.pyc │ ├── urls.cpython-311.pyc │ ├── urls.cpython-313.pyc │ ├── views.cpython-311.pyc │ └── views.cpython-313.pyc ├── admin.py ├── apps.py ├── forms.py ├── management │ └── commands │ ├── pycache │ │ ├── extract_activities.cpython-313.pyc │ │ └── insert_random_activities.cpython-313.pyc │ ├── extract_activities.py │ └── insert_random_activities.py ├── migrations │ ├── 0001_initial.py │ ├── 0002_activity_activity_type.py │ ├── 0003_recommendation.py │ ├── init.py │ └── pycache │ ├── 0001_initial.cpython-311.pyc │ ├── 0001_initial.cpython-313.pyc │ ├── 0002_activity_activity_type.cpython-311.pyc │ ├── 0002_activity_activity_type.cpython-313.pyc │ ├── 0003_recommendation.cpython-313.pyc │ ├── init.cpython-311.pyc │ └── init.cpython-313.pyc ├── models.py ├── tests.py ├── urls.py └── views.py db.sqlite3 duration_summary.csv fitness ├── init.py ├── pycache │ ├── init.cpython-311.pyc │ ├── init.cpython-313.pyc │ ├── settings.cpython-311.pyc │ ├── settings.cpython-313.pyc │ ├── urls.cpython-311.pyc │ ├── urls.cpython-313.pyc │ ├── wsgi.cpython-311.pyc │ └── wsgi.cpython-313.pyc ├── asgi.py ├── settings.py ├── urls.py └── wsgi.py manage.py merged_activities.csv requirements.txt sport_activities.csv templates ├── activityapp │ ├── activity_confirm_delete.html │ ├── activity_form.html │ └── activity_list.html ├── base.html ├── insert_random_activities.py └── userapp ├── login.html └── register.html userapp ├── init.py ├── pycache │ ├── init.cpython-311.pyc │ ├── init.cpython-313.pyc │ ├── admin.cpython-311.pyc │ ├── admin.cpython-313.pyc │ ├── apps.cpython-311.pyc │ ├── apps.cpython-313.pyc │ ├── forms.cpython-311.pyc │ ├── forms.cpython-313.pyc │ ├── models.cpython-311.pyc │ ├── models.cpython-313.pyc │ ├── urls.cpython-311.pyc │ ├── urls.cpython-313.pyc │ ├── views.cpython-311.pyc │ └── views.cpython-313.pyc ├── admin.py ├── apps.py ├── forms.py ├── migrations │ ├── 0001_initial.py │ ├── init.py │ └── pycache │ ├── 0001_initial.cpython-311.pyc │ ├── 0001_initial.cpython-313.pyc │ ├── init.cpython-311.pyc │ └── init.cpython-313.pyc ├── models.py ├── tests.py ├── urls.py └── views.py
This structure gives a clear overview of the project organization, with directories for apps (activityapp, fitness, and userapp) and configuration files. Each app contains its own migrations, views, models, forms, etc., for modular development. The root directory includes essential files like `manage.py`, `requirements.txt`, and `README.md`. However those csv files will come after extracting_activities as shown below

---

## Getting Started

To get a local copy of the **Fitness Tracking System** running, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fitness-tracking-system.git

2. Navigate to the project directory
   ```bash
   cd fitness-tracking-system
3. Install the required dependencies
   ```bash
   pip install -r requirements.txt
4. Setup the database
   If you're using PostgreSQL, make sure to adjust the settings.py file accordingly. Then, apply the migrations to set up the database schema.
   ```bash
   python manage.py migrate

5. Start the Django development server
    Make sure you Visit http://127.0.0.1:8000/register in your browser to begin  registration after running the server.

   ```bash
   python manage.py runserver


6. Insert random activities data
   ```bash
   python manage.py insert_random_activities
7. Export your data into CSV file 
   ```bash
   python manage.py extract_activities   
