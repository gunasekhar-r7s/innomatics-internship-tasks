# URL Shortener Web Application

A simple URL Shortener web application built using **Flask**, **SQLite**, and **SQLAlchemy**.  
The application converts long URLs into shorter ones, stores them in a database, and allows users to view their URL history.

---

## 📌 Features

- Shortens long URLs into easy-to-share short URLs  
- Redirects short URLs to the original URLs  
- Stores original and shortened URLs in a database  
- Displays URL history on a separate page  
- Validates user input URLs  
- Prevents duplicate short URL generation  

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS

### Backend
- Python
- Flask

### Database
- SQLite

### ORM
- SQLAlchemy

---

## 📂 Project Structure

url_shortener/
│
├── app.py
├── urls.db
│
├── templates/
│ ├── index.html
│ └── history.html
│
├── static/
│ └── style.css
│
└── README.md


---

## ⚙️ Installation & Setup

Follow the steps below to run the project locally:

### 1️⃣ Clone or Download the Project

git clone <repository-url>

or download the ZIP file and extract it.

### 2️⃣ Create Virtual Environment

python -m venv venv

Activate the virtual environment:

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

### 3️⃣ Install Dependencies

pip install flask flask_sqlalchemy

### 4️⃣ Run the Application

Open browser and visit:

http://127.0.0.1:5000/

### 🔄 How It Works

-- User enters a long URL on the home page   
-- URL is validated for correctness   
-- A random short code is generated   
-- Original URL and short code are saved in the database   
-- Short URL is displayed to the user  
-- Accessing the short URL redirects to the original URL   
-- History page shows all previously shortened URLs   

| Route           | Description                   |
| --------------- | ----------------------------- |
| `/`             | Home page for shortening URLs |
| `/<short_code>` | Redirects to original URL     |
| `/history`      | Displays URL history          |

📜 License

This project is created for educational purposes only.

👨‍💻 Author

Gunasekhar
