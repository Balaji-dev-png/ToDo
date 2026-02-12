📝 Django Work Heading & Task Manager

A clean, functional To-Do application built with Django and PostgreSQL. This app allows you to organize your daily tasks under custom "Work Headings" (Categories) for better productivity and structure.
🚀 Features

    Work Headings (Categories): Create specific groups for different projects or areas of life (e.g., "Personal," "Django Project," "Office").

    Task Management: Add tasks with titles and descriptions directly into specific headings.

    Automated Cleanup: Built with database-level cascading, so deleting a main heading automatically removes all tasks associated with it.

    Simple Completion: No complex status toggles—simply delete a task once you've finished it.

    Modern UI: Styled with a clean, responsive CSS layout.

🛠️ Tech Stack

    Backend: Python 3.13.1, Django 6.0.1

    Database: PostgreSQL 18

    Frontend: HTML5, CSS3

📂 Project Structure
Plaintext

ToDo/
├── static/          # style.css (Custom styling)
├── templates/       # HTML layouts (categorylist, tasklist, taskform, taskdelete)
├── todolist/        # Django project configuration (settings.py, urls.py)
└── todo/            # Task application (models.py, views.py, forms.py)

⚙️ Installation & Setup

    Clone the repository:
    Bash

    git clone https://github.com/Balaji-dev-png/ToDo.git
    cd ToDo

    Create and activate a virtual environment:
    Bash

    python -m venv .venv
    # Windows:
    .venv\Scripts\activate

    Install dependencies:
    Bash

    pip install django psycopg2

    Database Configuration: Ensure you have a PostgreSQL database named postgres with user postgres. Update your settings.py if your local credentials differ.

    Run Migrations:
    Bash

    python manage.py makemigrations
    python manage.py migrate

    Start the Server:
    Bash

    python manage.py runserver
