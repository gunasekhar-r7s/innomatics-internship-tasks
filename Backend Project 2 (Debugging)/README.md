# Backend Project 2 – Debugging (Flask Notes App)

## 📌 Project Overview
This project is a simple **Note Taking Web Application** built using **Flask**.  
The application contains a single home route (`/`) where users can add notes using a text field and button.  
All added notes are displayed on the same page as an unordered list.

The original code provided was **broken** and required debugging and refactoring to make the application work correctly.

---

## ⚙️ Tech Stack
- Python
- Flask
- HTML (Jinja2 Template)

---

## 🚀 Features
- Single home route (`/`)
- Add notes using a form
- Display all notes dynamically
- Notes persist during app runtime

---

## 🐞 Bugs Identified & Fixed

### 1. Route Method Issue
**Problem:**  
The home route only accepted `POST` requests, causing a *Method Not Allowed* error on page load.

**Fix:**  
Allowed both `GET` and `POST` methods.

---

### 2. Incorrect Data Retrieval
**Problem:**  
`request.args` was used to retrieve form data sent via POST.

**Fix:**  
Replaced with `request.form.get()`.

---

### 3. Missing Form Method
**Problem:**  
HTML form did not specify a method, defaulting to GET.

**Fix:**  
Explicitly set `method="POST"` in the form.

---

### 4. Appending Empty Notes
**Problem:**  
`None` values were added to the notes list.

**Fix:**  
Added a condition to append notes only if input is not empty.

---

### 5. No Initial Page Rendering
**Problem:**  
The page did not render properly on the initial GET request.

**Fix:**  
Handled GET requests to render the template with existing notes.

---

▶️ How to Run the Project

Install Flask:

pip install flask


Run the application:

python app.py


Open browser and visit:

http://127.0.0.1:5000/

👨‍💻 Author

Gunasekhar
