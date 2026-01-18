# Regex Matcher – Backend Project (Flask)

## Project Overview     

This project is a backend web application developed using **Python and Flask** that replicates the **core functionality of regex101.com**.          

The application allows users to enter a **test string** and a **regular expression**, and then displays **all matching results** after submitting the form.           

This project was created as part of **Backend Project 1 (Development)** during the **Data Science with Advanced GenAI Internship** at **Innomatics Research Labs**.              

---

## Objective

- To understand backend development using Flask        
- To work with Python regular expressions            
- To process user input and display dynamic results           

---

## Tech Stack

- **Language:** Python         
- **Framework:** Flask        
- **Frontend:** HTML (Jinja2 Templates)         
- **Regex Handling:** Python `re` module          

---

## Features

- Input field for test string          
- Input field for regular expression           
- Displays all regex matches           
- Handles invalid regex errors gracefully              
- Simple and user-friendly interface           

---

## Project Structure
regex_app/
│── app.py
│── templates/
│ └── index.html
│── README.md

## How to Run the Project

### Step 1: Install Flask

pip install flask

### Step 2: Run the Application

python app.py

### Step 3: Open in Browser

http://127.0.0.1:5000/

Example:

Test String: My email is test@gmail.com and admin@yahoo.com

Regular Expression: \b[\w.-]+@[\w.-]+\.\w+\b

Output:

test@gmail.com  
admin@yahoo.com

👨‍💻 Author

Gunasekhar
