# Fitness Tracking System

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)

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

fitness_tracking_system/ ├── .idea/ # IDE configuration files ├── .vscode/ # VS Code configuration files ├── activityapp/ # Main app for activity-related features │ ├── management/ # Custom management commands │ ├── migrations/ # Database migration files │ ├── pycache/ # Cached Python files │ ├── admin.py # Admin configuration for activity app │ ├── apps.py # App configuration │ ├── forms.py # Forms for activity-related inputs │ ├── models.py # Models for activity-related data │ ├── tests.py # Test cases for activity app │ ├── urls.py # URL routing for activity app │ └── views.py # Views for rendering activity-related data ├── fitness/ # Main app for fitness tracking features │ ├── pycache/ # Cached Python files │ ├── asgi.py # ASGI configuration │ ├── settings.py # Django settings │ ├── urls.py # URL routing for fitness app │ └── wsgi.py # WSGI configuration ├── userapp/ # App for user-related features │ ├── migrations/ # Database migration files │ ├── pycache/ # Cached Python files │ ├── admin.py # Admin configuration for user app │ ├── apps.py # App configuration │ ├── forms.py # Forms for user-related inputs │ ├── models.py # Models for user-related data │ ├── tests.py # Test cases for user app │ ├── urls.py # URL routing for user app │ └── views.py # Views for rendering user-related data ├── .gitignore # Git ignore rules ├── db.sqlite3 # SQLite database (if used locally) ├── duration_summary.csv # CSV file for duration summary ├── manage.py # Django project management file ├── merged_activities.csv # CSV file for merged activity data ├── README.md # Project documentation ├── requirements.txt # Python dependencies └── sport_activities.csv # CSV file for sport activities data



This structure gives a clear overview of the project organization, with directories for apps (activityapp, fitness, and userapp) and configuration files. Each app contains its own migrations, views, models, forms, etc., for modular development. The root directory includes essential files like `manage.py`, `requirements.txt`, and `README.md`.

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
   ```bash
   python manage.py runserver

Visit http://127.0.0.1:8000/register in your browser to begin  registration.
