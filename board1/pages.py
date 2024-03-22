from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from board1.models import User

from . import db

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    """Website Home route """
    return render_template("pages/home.html")

@bp.route("/profile")
def profile():
    """Website Profile route """
    return render_template("pages/profile.html")

@bp.route("/about")
def about():
    """Website about page route"""
    return render_template("pages/about.html")

@bp.route('/signup')
def signup():
    """Website signup page route"""
    return render_template('pages/signup.html')

@bp.route('/signup', methods=['POST'])
def signup_post():
    """Submits webform to the database
        And redirects user to login page if they exist
    """

    #values to add to the db
    email = request.form.get('email')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    password = request.form.get('password')

    #check if user already exists
    user = User.query.filter_by(email=email).first()

    #redirects user to signup page to retry
    if user:
        flash("Email address already exists", category='error')
        return redirect(url_for('pages.signup'))
    
     # Validate form fields
    if not email or not firstname or not lastname or not password:
        flash("Please fill out all fields", category='error')
        return redirect(url_for('pages.signup'))

    
    #create new user
    new_user = User(email=email, firstname=firstname, lastname=lastname, password=generate_password_hash(password))

    #add new user to the db
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('pages.login'))

@bp.route('/login')
def login():
    """Website login page route"""
    return render_template('pages/login.html')

@bp.route('/logout')
def logout():
    """Website logout page route"""
    return render_template('pages/logout.html')