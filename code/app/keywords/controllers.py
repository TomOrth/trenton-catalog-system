"""
Controller for the keywords

By: Matthew Van Soelen
"""

from app.keywords.model import Keyword
from app.setup import conn
from app.keywords.forms import SearchForm, KeywordForm
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash, Response, send_from_directory
from flask_login import login_required, current_user
from app.decorators import librarian
import psycopg2

keywords = Blueprint("keywords", __name__, url_prefix="/keywords")

# Display all keywords
@keywords.route("/search", methods=["GET","POST"])
@login_required
def all():
    query = f"SELECT * FROM keywords;"
    # Retrieve all keywords 
    keywords_res = Keyword.run_and_return_many(conn, query)
    search_form = SearchForm(request.form) # Search Form
    if request.method == "POST" and search_form.validate_on_submit: # If POST request, we redirect to GET but with query string
        return redirect(url_for("keywords.all", search=search_form.search.data))
    else:
        # We parse the query string to return the proper elements
        search_query = f"SELECT * FROM keywords;"
        # Were removing single quotes for parsing reasons
        search_string = request.args.get("search")
        if search_string != None:
            search_string = search_string.replace("'", "")

        if search_string is None or search_string == '':
            search_query = f"SELECT * FROM keywords"
        else:
            search_query = f"SELECT * FROM keywords WHERE keyword ILIKE \'%{search_string}%\'"
        keywords_res = Keyword.run_and_return_many(conn, search_query)

    return render_template("keywords/search.html", form=search_form, lflag=current_user.lflag, data=keywords_res, title="ALL", loggedin=current_user.is_authenticated, email=current_user.email)

# Enter a new keyword
@keywords.route("/new", methods=["GET","POST"])
@login_required
@librarian
def new():
    form = KeywordForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        try:
            _, res = conn.execute_and_return(f"SELECT * FROM keywords WHERE keyword=\'{form.keyword.data}\';")
            if len(res) < 1:
                conn.execute(f"INSERT INTO keywords(keyword) VALUES (\'{form.keyword.data}\');")
            else:
                flash("Keyword already exists")
                return redirect(url_for("keywords.new"))
            return redirect(url_for("keywords.all"))
        except (psycopg2.OperationalError, psycopg2.errors.UniqueViolation) as e:
            flash(f"Error: {e}")
            conn.rollback()
            return redirect(url_for("keywords.new"))
    return render_template("keywords/new.html", title="New Keywords", lflag=current_user.lflag,  form=form, loggedin=current_user.is_authenticated, email=current_user.email)

# Delete a keyword
@keywords.route("/delete", methods=["POST"])
@login_required
@librarian
def delete():
    id = request.form["id"]
    try:
        conn.execute(f"DELETE FROM describes WHERE k_id={id};")
        conn.execute(f"DELETE FROM keywords WHERE k_id={id};")
        return Response("Deleted", status=200)
    except psycopg2.OperationalError as e:
        flash(f"Error: {e}")
        return Response(f"Error: {e}", status=404)