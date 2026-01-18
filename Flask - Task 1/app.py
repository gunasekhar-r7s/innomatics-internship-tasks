from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Get the 'name' parameter from URL
    name = request.args.get('name')

    # Decide greeting based on time
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    # If name is provided, convert to uppercase
    if name:
        return f"<h1>{greeting}, {name.upper()}</h1>"
    else:
        return "<h1>Please provide a name using ?name=yourname</h1>"

if __name__ == '__main__':
    app.run(debug=True)
