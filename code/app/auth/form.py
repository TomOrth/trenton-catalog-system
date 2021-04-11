"""
Represents the Signup and Signin form used for authentication
"""
from flask_wtf import FlaskForm

# Import Form elements such as TextField and BooleanField
from wtforms import TextField, PasswordField, BooleanField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo


# Define the login form (WTForms)

class AuthForm(FlaskForm):
    """
    Class that represents the auth form a user uses
    """
    email    = TextField('Email Address', [Email(),
                Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
                Required(message='Must provide a password. ;-)')])

    lflag = BooleanField("Librarian?")