# URL Shortener Web Application (Advanced)

A URL Shortener web application built using **Flask (Python)** that allows users to **sign up, log in, shorten URLs, and view their personal URL history**. This project demonstrates backend development, authentication, database integration, and basic web application workflows.

---

## 📌 Features

- User Signup with username validation
- User Login and Logout using Flask-Login
- URL shortening functionality
- URL validation before shortening
- Redirection from short URL to original URL
- User-specific URL history
- SQLite database integration using SQLAlchemy

---

## 🛠️ Tech Stack

### Frontend
- HTML

### Backend
- Flask (Python)

### Authentication
- Flask-Login

### Database
- SQLite
- SQLAlchemy (ORM)

### Validation
- validators library

---

## 📁 Project Structure

url-shortener-flask/
│
├── app.py
├── requirements.txt
├── database.db
│
└── templates/
├── login.html
├── signup.html
└── home.html


---

## ⚙️ Installation & Setup

1️⃣ Create a virtual environment

python -m venv venv       
venv\Scripts\activate

2️⃣ Install dependencies 

pip install -r requirements.txt

3️⃣ Run the application

python app.py

4️⃣ Open in browser

http://127.0.0.1:5000/signup

📬 Author

Gunasekhar
