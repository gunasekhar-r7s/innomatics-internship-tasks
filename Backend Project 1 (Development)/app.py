from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    matches = []
    error = None

    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex_pattern']

        try:
            matches = re.findall(regex_pattern, test_string)
        except re.error as e:
            error = f"Invalid Regex: {e}"

    return render_template('index.html', matches=matches, error=error)

if __name__ == '__main__':
    app.run(debug=True)
