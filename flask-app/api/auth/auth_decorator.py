from flask import session, abort, request
from functools import wraps
from models import User
import jwt

def auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return abort(401)
        try:
            data = jwt.decode(token, "kdxhfds iefhsdbf", algorithms=["HS256"])
            current_user = User.query.filter_by(user_id = data['user_id']).first()
        except:
            return abort(401)
  
        return f(current_user, *args, **kwargs)
    return decorated_function