from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from board1.models import User, Profile
from board1 import db


bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    """Website Home route """
    return render_template("pages/home.html")


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
    firstname = request.form.get('first_name')
    lastname = request.form.get('last_name')
    password = request.form.get('password')

    
    #check if user already exists
    user = User.query.filter_by(email=email).first()

    #redirects user to signup page to retry
    if user:
        flash("Email address already exists", category='error')
        return redirect(url_for('pages.signup'))

    #create new user
    new_user = User(email=email, firstname=firstname, lastname=lastname, password=generate_password_hash(password))
    
    #add new user to the db
    db.session.add(new_user)
    db.session.commit()


    return redirect(url_for('pages.dashboard'))

@bp.route("/profile", methods=["POST", "GET"])
def profile():
    """Website profile page route"""
    if 'user_id' not in session:
        return redirect(url_for('pages.signin'))

    # Get the user ID from the session
    user_id = session['user_id']
    

    # Check if the user already has a profile
    existing_profile = Profile.query.filter_by(user_id=user_id).first()
    
    print(existing_profile)
    if request.method == "POST":
        current_job_title = request.form.get("current_job_title")
        desired_job = request.form.get("desired_job")
        work_experience = request.form.get("work_experience")
        education_level = request.form.get("education_level")
        certifications = request.form.get("certifications")
        portfolio = request.form.get("portfolio")
        technical_skills = request.form.get("technical_skills")
        industry_skills = request.form.get("industry_skills")
        preferred_company_size = request.form.get("preferred_company_size")
        desired_job_type = request.form.get("desired_job_type")
        salary_range = request.form.get("salary_range")
        job_location = request.form.get("job_location")
        willing_to_relocate = request.form.get("willing_to_relocate") == 'Yes'
        languages_spoken = request.form.get("languages_spoken")
        interest_hobbies = request.form.get("interest_hobbies")

        if existing_profile:
            # Update the existing profile
            existing_profile.current_job_title = current_job_title
            existing_profile.desired_job = desired_job
            existing_profile.work_experience = work_experience
            existing_profile.education_level = education_level
            existing_profile.certifications = certifications
            existing_profile.portfolio = portfolio
            existing_profile.technical_skills = technical_skills
            existing_profile.industry_skills = industry_skills
            existing_profile.preferred_company_size = preferred_company_size
            existing_profile.desired_job_type = desired_job_type
            existing_profile.salary_range = salary_range
            existing_profile.job_location = job_location
            existing_profile.willing_to_relocate = willing_to_relocate
            existing_profile.languages_spoken = languages_spoken
            existing_profile.interest_hobbies = interest_hobbies
            
        else:
            # Create a new profile
            
            new_profile = Profile(
                user_id=user_id,
                current_job_title=current_job_title,
                desired_job=desired_job,
                work_experience=work_experience,
                education_level=education_level,
                certifications=certifications,
                portfolio=portfolio,
                technical_skills=technical_skills,
                industry_skills=industry_skills,
                preferred_company_size=preferred_company_size,
                desired_job_type=desired_job_type,
                salary_range=salary_range,
                job_location=job_location,
                willing_to_relocate=willing_to_relocate,
                languages_spoken=languages_spoken,
                interest_hobbies=interest_hobbies
            )

            # Add the profile to the database
            db.session.add(new_profile)
        db.session.commit()
    return render_template("pages/profile.html")



@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    """Website login page route"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user exists
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("Incorrect email or password", category='error')
            return redirect(url_for('pages.signin'))

        # Validate password
        if not check_password_hash(user.password, password):
            flash("Incorrect email or password", category='error')
            return redirect(url_for('pages.signin'))

        # Login successful - Store user information in session
        session['user_id'] = user.id

        # Login successful - Redirect to dashboard
        return redirect(url_for('pages.dashboard'))
    
    return render_template('pages/signin.html')
@bp.route('/logout')
def logout():
    """Website logout page route"""
    return render_template('pages/logout.html')

@bp.route('/dashboard')
def  dashboard():
    return render_template('pages/dashboard.html')

@bp.route('/jobs')
def jobs():
    return render_template('pages/jobs.html')

@bp.route('/notifications')
def notifications():
    return render_template('pages/notifications.html')

@bp.route('/settings')
def settings():
    return render_template('pages/settings.html')