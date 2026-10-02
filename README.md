# hostel-management-system
A web-based Hostel Management System built with Django to manage hostel operations efficiently. This application provides features for managing students, rooms, complaints, fees, and notices — all from a centralized dashboard.

Features
Student Management — Register, view, and manage student profiles
Room Management — Allocate, assign, and track room availability
Complaint System — Students can raise complaints; admins can track and resolve them
Fee Management — Track fee payments, due amounts, and payment history
Notice Board — Post and view hostel announcements and notices
Authentication — Secure login and role-based access
Tech Stack
Backend
Django (Python)
Database
SQLite (default)
Frontend
HTML, CSS, JavaScript
Template Engine
Django Templates
Project Structure
hostel-management-system/
│
├── accounts/          # Authentication & user management
├── complaints/        # Complaint tracking system
├── fees/              # Fee management & payments
├── hostel_management/ # Core Django settings & configurations
├── media/             # Uploaded files (images, documents)
├── notice/            # Notice board functionality
├── rooms/             # Room allocation & management
├── students/          # Student profiles & records
├── templates/         # Reusable HTML templates
├── db.sqlite3         # SQLite database file
├── manage.py          # Django management script
└── README.md          # This file
Setup & Installation
1. Clone the Repository
bash

Copy
git clone https://github.com/NANI381C/hostel-management-system
cd hostel-management-system
2. Create a Virtual Environment
bash

Copy
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
3. Install Dependencies
bash

Copy
pip install -r requirements.txt
If requirements.txt doesn't exist, install manually:

bash

Copy
pip install django
4. Apply Migrations
bash

Copy
python manage.py makemigrations
python manage.py migrate
5. Create a Superuser (Admin)
bash

Copy
python manage.py createsuperuser
6. Run the Development Server
bash

Copy
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser.

Visit http://127.0.0.1:8000/admin to access the admin panel.

Usage
Admin logs in via /admin to manage all modules
Students can log in to:
View room details
Raise complaints
Check fee status
View notices
Staff can manage room allocations, resolve complaints, and post notices
Default Credentials
Create your own admin superuser using the createsuperuser command above. No default credentials are set.

Future Enhancements

 Payment gateway integration

 Email notifications for complaints & notices

 Mobile-responsive design

 Role-based dashboard with charts & analytics

 MySQL/PostgreSQL database support

 API endpoints (Django REST Framework)
Author
Simham Nagasai — NANI381C

License
This project is open source and available under the MIT License.

Feel free to customize it — let me know if you want to add screenshots, a demo link, or adjust any section!
