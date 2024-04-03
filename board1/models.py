from . import db
from flask_sqlalchemy  import SQLAlchemy

"""
user instance is a model for the user table in the database
"""

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    
    profile = db.relationship('Profile', backref='user', uselist=False)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

    current_job_title = db.Column(db.String(100))
    desired_job = db.Column(db.String(100))
    work_experience = db.Column(db.Text)
    education_level = db.Column(db.String(50))
    certifications = db.Column(db.String(200))
    portfolio = db.Column(db.String(200))
    technical_skills = db.Column(db.String(200))
    industry_skills = db.Column(db.String(200))
    preferred_company_size = db.Column(db.String(50))
    desired_job_type = db.Column(db.String(50))
    salary_range = db.Column(db.String(50))
    job_location = db.Column(db.String(100))
    willing_to_relocate = db.Column(db.Boolean)
    languages_spoken = db.Column(db.String(100))
    interest_hobbies = db.Column(db.Text)

    