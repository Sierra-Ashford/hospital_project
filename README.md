Hospital Management System

This is a Django-based hospital management system that handles patient records, doctor assignments, billing, and department management. 

SetUp Instructions

1. Create a Virtual Environment

2. Install Dependencies: pip install -r requirements.txt

3. Configure Database
    - Update settings.py with your database credentials.

4. Apply Migrations
    - python manage.py makemigrations
    - python manage.py migrate

5.  Create a Superuser (Admin Access)
    - python manage.py createsuperuser
    - Follow the prompts to set up an admin user.

6. Run the Development Server
    - python manage.py runserver
    - Visit http://127.0.0.1:8000/admin/ to access the Django admin panel