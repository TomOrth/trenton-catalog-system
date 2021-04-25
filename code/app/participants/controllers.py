# Controller for Participants.
# By: Justin Pabon

from app.participants.model import Participant
from app.setup import conn
from app.participants.forms import NewForm, SearchForm
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash, Response, send_from_directory
from flask_login import login_required, current_user
from app.decorators import librarian
import psycopg2

participants = Blueprint("participants", __name__, url_prefix="/participants")


# Show all participants.
@participants.route("/search", methods=["GET","POST"])
@login_required
def all():
    search_query = f"SELECT * FROM participants;"
    participants_res = Participant.run_and_return_many(conn, search_query)

    search_form = SearchForm(request.form) # Search Form

    if request.method == "POST" and search_form.validate_on_submit: # If POST request, we redirect to GET but with query string
        return redirect(url_for("participants.all", search=search_form.search.data))
    else:
        # We parse the query string to return the proper elements
        search_query = f"SELECT * FROM participants;"
        # Were removing single quotes for parsing reasons
        search_string = request.args.get("search")
        if search_string != None:
            search_string = search_string.replace("'", "")

        if search_string is None or search_string == '':
            search_query = f"SELECT * FROM participants"
        else:
            search_query = f"SELECT * FROM participants WHERE name ILIKE \'%{search_string}%\'"
        participants_res = Participant.run_and_return_many(conn, search_query)

    return render_template("participants/search.html", form=search_form, lflag=current_user.lflag, title="All Participants", loggedin=current_user.is_authenticated, email=current_user.email, data=participants_res)


# Present a form for the user to create a new participant.
@participants.route("/new", methods=["GET","POST"])
@login_required
@librarian
def new():
    new_form = NewForm(request.form)

    if request.method == "POST" and new_form.validate_on_submit():
        _, res = conn.execute_and_return(f"SELECT * FROM participants WHERE name=\'{new_form.name.data}\';")
        if len(res) < 1:
            conn.execute(f"INSERT INTO participants(name) VALUES (\'{new_form.name.data}\');")
        return redirect(url_for("participants.all"))

    return render_template("participants/new.html", title="New Participant", lflag=current_user.lflag, form=new_form, loggedin=current_user.is_authenticated, email=current_user.email)


# Delete Participant
@participants.route("/delete", methods=["POST"])
@login_required
@librarian
def delete():
    id = request.form["id"]
    try:
        conn.execute(f"DELETE FROM participates WHERE p_id={id};")
        conn.execute(f"DELETE FROM participants WHERE p_id={id};")
        return Response("Deleted", status=200)
    #return render_template("participants/delete.html", title="Delete Participant", loggedin=current_user.is_authenticated, email=current_user.email, data=participants_res)
    except psycopg2.OperationalError as e:
        return Response(f"Error: {e}", status=404)
