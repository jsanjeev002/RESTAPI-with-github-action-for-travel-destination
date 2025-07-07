# 🌍 Travel API

A RESTful API built with Flask and SQLAlchemy to manage travel destinations. This API supports full CRUD operations on travel destination data stored in a SQLite database.

---

## 🚀 Features

- Add new travel destinations (`POST /destinations`)
- Retrieve all destinations (`GET /destinations`)
- Retrieve a specific destination by ID (`GET /destinations/<id>`)
- Update an existing destination (`PUT /destinations/<id>`)
- Delete a destination (`DELETE /destinations/<id>`)

---

## 📁 Project Structure

Travel-api<br>
├── main.py               # Main Flask application<br> 
├── travel.db             # SQLite database (auto-created)<br>
├── requirements.txt      # Python dependencies <br>  
└── README.md             # Project documentation

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy

---

## 📦 Requirements

- Python 3.7+
- `pip` (Python package manager)

Install dependencies:

```bash
pip install -r requirements.txt