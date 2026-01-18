from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import validators
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# ================= MODELS =================

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(9), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    short_url = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# ================= LOGIN =================

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ================= ROUTES =================

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(username) < 5 or len(username) > 9:
            flash("Username must be between 5 to 9 characters long")
            return redirect('/signup')

        if User.query.filter_by(username=username).first():
            flash("This username already exists")
            return redirect('/signup')

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        flash("Signup successful. Please login.")
        return redirect('/login')

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username'],
            password=request.form['password']
        ).first()

        if user:
            login_user(user)
            return redirect('/')
        else:
            flash("Invalid credentials")

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


def generate_short():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    short_url = None

    if request.method == 'POST':
        original = request.form['url']

        if not validators.url(original):
            flash("Invalid URL")
            return redirect('/')

        short = generate_short()

        new = URL(
            original_url=original,
            short_url=short,
            user_id=current_user.id
        )
        db.session.add(new)
        db.session.commit()

        short_url = request.host_url + short

    urls = URL.query.filter_by(user_id=current_user.id).all()
    return render_template('home.html', short_url=short_url, urls=urls)


@app.route('/<code>')
def redirect_url(code):
    url = URL.query.filter_by(short_url=code).first_or_404()
    return redirect(url.original_url)


# ================= MAIN =================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
