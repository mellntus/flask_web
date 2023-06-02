from . import db
from .app.model.models import User
from .app.utility import utility

from flask import Blueprint, request
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)
get_utility = utility

"""
    Login
"""
@auth.route('/login')
def login():
    # check current user
    if current_user.is_authenticated:
        return get_utility.set_redirect_url_for_path("main.index")
    
    response = get_utility.get_and_make_response_for_path("login.html")
    return response

@auth.route('/login', methods=['POST'])
def login_post():
    
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        msg = "Please check your login details and try again."
        get_utility.set_flash(msg=msg)

        return get_utility.set_redirect_url_for_path("auth.login") # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    get_utility.set_login_user(user, remember=remember)
    return get_utility.set_redirect_url_for_path("main.profile")


"""
    Signup
"""
@auth.route('/signup')
def signup():
    # check current user
    if current_user.is_authenticated:
        return get_utility.set_redirect_url_for_path("main.index")
    
    response = get_utility.get_and_make_response_for_path("signup.html")
    return response

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        msg = "Email address already exists"
        get_utility.set_flash(msg=msg)
        
        return get_utility.set_redirect_url_for_path("auth.signup") 

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return get_utility.set_redirect_url_for_path("auth.login")


"""
    Logout
"""
@auth.route('/logout')
@login_required
def logout():
    get_utility.set_logout_user()

    return get_utility.set_redirect_url_for_path("main.index")