from flask import Flask, render_template, redirect, url_for
from app.auth.controllers import auth
from app.auth.model import User

from app.transcripts.controllers import transcripts

from app.setup import conn
from flask_login import LoginManager, current_user

# Basic Flask Setup
app = Flask(__name__)
login_manager = LoginManager(app)
app.config["CSRF_ENABLED"] = True
app.config["SECRET_KEY"] = "Secret"
app.config['UPLOAD_FOLDER'] = "uploads"

# We have to register each blueprint
app.register_blueprint(auth)
app.register_blueprint(transcripts)

# Main endpoint for the application
@app.route("/")
def main():
    email = ""
    if current_user.is_authenticated:
        email = current_user.email
    return render_template("index.html", title="Home", loggedin=current_user.is_authenticated, email=email)

# Load the current user
@login_manager.user_loader
def load_user(user_id):
    return User.run_and_return(conn, f"SELECT * FROM users WHERE user_id=\'{user_id}\'")

# Redirect unauthorized access to signin
@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for("auth.signin"))

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()