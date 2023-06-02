"""
    Other function for helper goes here
"""

# Delete cache
def get_and_make_response_for_path(path:str):
    """
        Format path => {file}.html
        Return response
    """
    from flask import make_response, render_template
    
    response = make_response(render_template(f'{path}'))
    response = set_delete_cache(response)
    return response

def set_delete_cache(response):
    response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return response


# Set redirect url for path
def set_redirect_url_for_path(path:str):
    """
        Format path => {file}.{def} > File name without .py
        Return redirect
    """
    from flask import redirect, url_for

    return redirect(url_for(f'{path}'))


# Set flash here
def set_flash(msg:str):
    """
        Set flash message goes here
        Return Nothing
    """
    from flask import flash

    flash(msg)


# Set login user
def set_login_user(user, remember:bool=False):
    """
        Set login user goes here
        Return Nothing
    """
    from flask_login import login_user

    login_user(user, remember=remember)


# Set logout user
def set_logout_user():
    """
        Set logout user goes here
        Return Nothing
    """
    from flask_login import logout_user

    logout_user()
