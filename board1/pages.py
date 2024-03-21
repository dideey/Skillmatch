from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route('/signup')
def signup():
    return render_template('pages/signup.html')

@bp.route('/login')
def login():
    return render_template('pages/login.html')