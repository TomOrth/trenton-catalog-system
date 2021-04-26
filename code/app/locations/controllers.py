"""
Controller for the locations

By: Matthew Van Soelen
"""

from app.locations.model import Location
from app.setup import conn
from app.locations.forms import SearchForm, LocationForm
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash, Response, send_from_directory
from flask_login import login_required, current_user
from app.decorators import librarian
import psycopg2

locations = Blueprint("locations", __name__, url_prefix="/locations")

# Display all locations
@locations.route("/search", methods=["GET","POST"])
@login_required
def all():
    query = f"SELECT * FROM locations;"
    # Retrieve all keywords 
    locations_res = Location.run_and_return_many(conn, query)
    search_form = SearchForm(request.form) # Search Form
    if request.method == "POST" and search_form.validate_on_submit: # If POST request, we redirect to GET but with query string
        return redirect(url_for("locations.all", search=search_form.search.data))
    else:
        # We parse the query string to return the proper elements
        search_query = f"SELECT * FROM locations;"
        # Were removing single quotes for parsing reasons
        search_string = request.args.get("search")
        if search_string != None:
            search_string = search_string.replace("'", "")

        if search_string is None or search_string == '':
            search_query = f"SELECT * FROM locations"
        else:
            search_query = f"SELECT * FROM locations WHERE street_name ILIKE \'%{search_string}%\'"
        locations_res = Location.run_and_return_many(conn, search_query)

    return render_template("locations/search.html", form=search_form, lflag=current_user.lflag, data=locations_res, title="ALL", loggedin=current_user.is_authenticated, email=current_user.email)

# Enter a new locations
@locations.route("/new", methods=["GET","POST"])
@login_required
@librarian
def new():
    form = LocationForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        try:
            _, res = conn.execute_and_return(f"SELECT * FROM locations WHERE street_name=\'{form.location.data}\';")
            if len(res) < 1:
                conn.execute(f"INSERT INTO locations(street_name) VALUES (\'{form.location.data}\');")
            else:
                flash("Location already exists")
                return redirect(url_for("locations.new"))
            return redirect(url_for("locations.all"))
        except (psycopg2.OperationalError, psycopg2.errors.UniqueViolation) as e:
            flash(f"Error: {e}")
            conn.rollback()
            return redirect(url_for("locations.new"))
    return render_template("locations/new.html", title="New Locations", lflag=current_user.lflag, form=form, loggedin=current_user.is_authenticated, email=current_user.email)

# Delete a location
@locations.route("/delete", methods=["POST"])
@login_required
@librarian
def delete():
    id = request.form["id"]
    try:
        conn.execute(f"DELETE FROM mentions WHERE location_id={id};")
        conn.execute(f"DELETE FROM locations WHERE location_id={id};")
        return Response("Deleted", status=200)
    except psycopg2.OperationalError as e:
        flash(f"Error: {e}")
        return Response(f"Error: {e}", status=404)