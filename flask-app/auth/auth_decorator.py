from flask import session, request, redirect, url_for
from functools import wraps

def auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'email' in session:
            return redirect(url_for('auth_page.sign_in', next=request.url))
        return f(*args, **kwargs)
    return decorated_function