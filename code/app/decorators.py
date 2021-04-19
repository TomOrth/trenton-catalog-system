"""
These are extra decorators meant for the different routes in the controllers

By: Tom Orth
"""

from functools import wraps
from flask import request, redirect, url_for, flash
from flask_login import current_user

def librarian(f):
    """
    Checks to see if the user is a librarian for certain routes
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.lflag == 0:
            flash("You are not a librarian! Please sign in to a librarian account")
            return redirect(url_for('main'))
        return f(*args, **kwargs)
    return decorated_function