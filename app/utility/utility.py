"""
    Other function for helper goes here
"""
def after_request(response):
    response.headers["Cache-Control"] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    return response