from .app.utility import utility

from flask import Blueprint, make_response, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)
get_utility = utility

@main.route('/')
def index():
    response = get_utility.get_and_make_response_for_path("index.html")
    return response

@main.route('/profile')
@login_required
def profile():
    # check current user
    if not current_user.is_authenticated:
        return get_utility.set_redirect_url_for_path("main.index")
    
    response = make_response(render_template('profile.html', name=current_user.name))
    response = get_utility.set_delete_cache(response)
    return response