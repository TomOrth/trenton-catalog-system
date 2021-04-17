"""
Controller for the keywords

By: Matthew Van Soelen
"""

from app.locations.model import Location
from app.setup import conn
from app.locations.form import SearchForm
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash, Response, send_from_directory
from flask_login import login_required, current_user

locations = Blueprint("locations", __name__, url_prefix="/locations")

@locations.route("/list", methods=["GET", "Post"])
@login_required

def list():
    search_form = SearchForm(request.form) # Search Form
    if request.method == "POST" and search_form.validate_on_submit:
        return redirect(url_for("locations.list", search=search_form.search.data))
    else:
        # We parse the query string to return the proper elements
        search_string = request.args.get("search")
        search_query = f"SELECT * FROM location_transcript_view WHERE street_name ILIKE \'{search_string}\'"

        # After retrieving the transcripts, we parse them into dictionarys to be sent back to the main screen
        transcripts_res = Location.run_and_return_many(conn, search_query)
        transcripts_dicts = [transcript.__dict__ for transcript in transcripts_res]

        for i, transcript in enumerate(transcripts_dicts):
            transcripts_dicts[i] = transcript
        return render_template("locations/list.html", title="Location", form=search_form, loggedin=current_user.is_authenticated, email=current_user.email, data=transcripts_dicts)
