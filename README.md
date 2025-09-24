# ✯ Simple To-Do List Manager ✯

A lightweight task manager with REST API + retro-styled web interface

# Overview

This project is a full-stack To-Do List Manager built with Flask (Python), SQLite (via SQLAlchemy), and a simple HTML/JavaScript frontend.

It started as a console program and was restructured into a proper web application with:

Clear backend architecture (routes, services, models)

A retro style GUI

REST API for external clients

Automated unit tests (pytest)

Ready for Docker & CI/CD pipelines

# Features

Add, View, Edit, Complete, Delete tasks

Search tasks by keyword

Web GUI (retro styled list & table view)

REST API (JSON endpoints)

Unit tests with pytest

Docker-ready (containerized deployment)

CI/CD ready (GitHub Actions workflow example)

# Project Structure

Simple-To-Do-List-Manager/

│

├── backend/

│   ├── app.py              # Flask entrypoint

│   ├── routes/             # API route definitions

│   ├── services/           # Business logic

│   ├── models/             # SQLAlchemy models

│   ├── database.py         # DB setup & session

│   └── tests/              # Pytest unit tests

│

├── templates/

│   ├── index.html          # Main web frontend

│

├── requirements.txt        # Python dependencies

├── Dockerfile              # Container build (optional)

├── docker-compose.yml      # Local dev stack (optional)

└── README.md               # Project documentation

 # API Endpoints
Method	Endpoint	Description
GET	/tasks/	List all tasks (HTML or JSON)
POST	/tasks/	Add a new task
GET	/tasks/<id>	Get task by ID
PUT	/tasks/<id>	Edit/update a task
PUT	/tasks/<id>/complete	Mark as complete
PATCH	/tasks/<id>/toggle	Toggle complete status
DELETE	/tasks/<id>	Delete task
GET	/tasks/search?q=foo	Search tasks by title


# Frontend

Visit http://127.0.0.1:5000/tasks/ → tasks displayed in a table view

Visit http://127.0.0.1:5000/ → main retro list UI with add/search/edit/delete

# Setup & Run

1. Clone repo & create virtual env
```bash
git clone https://github.com/<your-username>/Simple-To-Do-List-Manager.git
cd Simple-To-Do-List-Manager
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```
2. Run locally
```bash
export FLASK_APP=backend.app   # (Windows: set FLASK_APP=backend.app)
flask run
```


Visit: http://127.0.0.1:5000
