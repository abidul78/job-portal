# JobPortal

A Django-based recruitment platform for job seekers and employers.

## Features

### Job Seeker

- Create account and login
- Browse available jobs
- Search by keyword, company, and location
- Apply for jobs
- Prevent duplicate applications
- Track application status
- View My Applications
- Create applicant profile
- Add phone, skills, education, experience, and bio
- Upload resume
- Use JobPortal assistant chatbot

### Employer

- Create employer account
- Post jobs
- Edit and delete jobs
- View employer dashboard
- View applicants for each job
- View applicant profiles
- View applicant resumes
- Update application status:
  - Pending
  - Shortlisted
  - Selected
  - Rejected

## Tech Stack

- Python
- Django
- HTML
- CSS
- Bootstrap 5
- SQLite
- JavaScript

## Project Structure

```text
job_portal/
│
├── accounts/
├── jobs/
├── config/
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

Installation
Clone the repository:
git clone YOUR_REPOSITORY_URL

Go to the project directory:
cd job_portal

Create a virtual environment:
py -3.11 -m venv venv

Activate it on Windows:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Create a .env file:
SECRET_KEY=your_secret_key_here
DEBUG=True

Run migrations:
python manage.py migrate

Start the development server:
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

User Roles
Job Seeker
Can search and apply for jobs, manage a profile, upload a resume, and track application status.
Employer
Can post and manage jobs, review applicants, view applicant profiles and resumes, and update application status.
Application Status
Applications can have the following status:
- Pending
- Shortlisted
- Selected
- Rejected
Search and Pagination
Users can search jobs using:
- Job title / keyword
- Company
- Location
Job listings are paginated for better usability.
Environment Variables
Sensitive values such as the Django secret key are stored in .env.
Do not commit .env to GitHub.
Future Improvements
- PostgreSQL database
- Email notifications
- Password reset
- Saved jobs
- REST API
- AI-powered job recommendations
- Production deployment
Author
Abidul Islam