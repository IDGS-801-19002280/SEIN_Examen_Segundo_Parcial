from functools import wraps
from flask import request, redirect, url_for
from flask_login import current_user

def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('tienda.index'))
        else:
            return f(*args, **kwargs)
    return decorated_function