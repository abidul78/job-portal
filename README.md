# JobPortal

A Django-based recruitment platform for job seekers and employers.

## Live Demo

https://jobportal-vpw3.onrender.com

## Features

### Job Seeker

- Create an account and login
- Browse available jobs
- Search jobs by keyword, company, and location
- View job details
- Apply for jobs
- Prevent duplicate job applications
- Track application status
- View My Applications
- Create and update applicant profile
- Add phone number, skills, education, experience, and bio
- Upload resume
- Use the JobPortal assistant chatbot

### Employer

- Create an employer account
- Login securely
- Post new jobs
- Edit own job posts
- Delete own job posts
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
- PostgreSQL
- HTML
- CSS
- Bootstrap 5
- JavaScript
- WhiteNoise
- Gunicorn
- Render

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
├── Procfile
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/abidul78/job-portal.git
```

### 2. Go to the project directory

```bash
cd job-portal
```

### 3. Create a virtual environment

```bash
py -3.11 -m venv venv
```

### 4. Activate the virtual environment on Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## PostgreSQL Setup

Create a PostgreSQL database and user.

```sql
CREATE DATABASE jobportal_db;
CREATE USER jobportal_user WITH PASSWORD 'your_password';
ALTER DATABASE jobportal_db OWNER TO jobportal_user;
```

## Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=jobportal_db
DB_USER=jobportal_user
DB_PASSWORD=your_database_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

Do not commit the `.env` file to GitHub.

## Run Migrations

```bash
python manage.py migrate
```

## Start the Development Server

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

## User Roles

### Job Seeker

Job seekers can search and apply for jobs, manage their profile, upload a resume, and track application status.

### Employer

Employers can post and manage jobs, review applicants, view applicant profiles and resumes, and update application status.

## Application Status

Applications can have the following status:

- Pending
- Shortlisted
- Selected
- Rejected

## Search and Pagination

Users can search jobs using:

- Job title or keyword
- Company name
- Location

Job listings are paginated for better usability.

## Security

Sensitive configuration values such as:

- Django Secret Key
- Database credentials
- Debug setting

are stored using environment variables.

The `.env` file is excluded from Git using `.gitignore`.

## Deployment

The project is deployed on Render.

Production setup includes:

- PostgreSQL database
- Gunicorn WSGI server
- WhiteNoise for static files
- Environment-based configuration
- Render Web Service

## Live Website

https://jobportal-vpw3.onrender.com

## Future Improvements

- Email notifications
- Password reset
- Saved jobs
- REST API
- AI-powered job recommendations
- Email verification
- Job categories
- Company profiles

## Author

Abidul Islam