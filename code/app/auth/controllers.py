"""
Represents the routes and controllers for authenthication

By: Tom Orth
"""
from app.auth.model import User
from app.auth.form import AuthForm
from app.setup import conn
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
from flask_login import login_user, logout_user
import bcrypt

# Sets up the Blueprint
auth = Blueprint("auth", __name__, url_prefix="/auth")

# Signup route for a user
@auth.route("/signup", methods=["GET", "POST"])
def signup():

    # Construct a form
    signup_form = AuthForm(request.form)

    # Handle a post request
    if request.method == "POST" and signup_form.validate_on_submit():

        # Check if user exists
        _, content = conn.execute_and_return(f"SELECT * FROM users WHERE email=\'{signup_form.email.data}\'")

        # If it does not, we insert into the database, construct the User object and login the user
        if len(content) == 0:
            password_hash = bcrypt.hashpw(bytes(signup_form.password.data, "utf-8"), bcrypt.gensalt()).decode("utf-8")
            lflag = int(signup_form.lflag.data)
            _, col = conn.execute_and_return(f"INSERT INTO users(email, password_hash, lflag) VALUES (\'{signup_form.email.data}\', \'{password_hash}\', \'{lflag}\') RETURNING user_id")
            user = User(int(col[0][0]), signup_form.email.data, password_hash, lflag)
            login_user(user)
            return redirect(url_for("main"))
        # If it does exist, we flash a message to the user
        else:
            flash("User exists already")
            return redirect(url_for("auth.signup"))
    return render_template("auth/signup.html", title="Sign-up", form=signup_form)

# Route to signin
@auth.route('/signin', methods=["GET", "POST"])
def signin():

    # Instantiate the form
    signin_form = AuthForm(request.form)

    # Handle the post request
    if request.method == "POST" and signin_form.validate_on_submit():

        # Check if the user exists
        _, content = conn.execute_and_return(f"SELECT COUNT(user_id) FROM users WHERE email=\'{signin_form.email.data}\'")
        count = content[0][0]

        # If it does, we construct the object
        if count > 0:
            user = User.run_and_return(conn, f"SELECT * FROM users WHERE email=\'{signin_form.email.data}\'")

            # We check the hash, if it matches, we login
            if bcrypt.checkpw(bytes(signin_form.password.data, "utf-8"), bytes(user.password_hash, "utf-8")):
                login_user(user)
                return redirect(url_for("main"))
            
            # If it doesn't match, we flash a warning
            else:
                flash("Incorrect Password")
                return redirect(url_for("auth.signin"))
        # If the user doesn't exist, we flash a message
        else:
            flash("User does not exist. Please check the email you entered")
            return redirect(url_for("auth.signin"))

    return render_template("auth/signin.html", title="Sign-in", form=signin_form)

# Route to logout
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main"))
