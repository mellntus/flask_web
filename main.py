from . import db
from .app.utility import utility
from flask import Blueprint, make_response, redirect, render_template, url_for
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return response

@main.route('/profile')
@login_required
def profile():
    # check current user
    if not current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    response = make_response(render_template('profile.html', name=current_user.name))
    response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return response