"""
Controller for the transcripts (full info)

By: Tom Orth
"""

from app.transcripts.model import FullTranscript
from app.utils import convert_full_transcripts_to_json, check_if_parsed_transcripts_are_bookmarked
from app.transcripts.form import SearchForm
from app.setup import conn
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash, Response, send_from_directory
from flask_login import login_required, current_user


transcripts = Blueprint("transcripts", __name__, url_prefix="/transcripts")

# Search page for transcripts
@login_required
@transcripts.route("/search", methods=["GET", "POST"])
def search():
    search_form = SearchForm(request.form) # Search Form
    if request.method == "POST" and search_form.validate_on_submit: # If POST request, we redirect to GET but with query string
        return redirect(url_for("transcripts.search", category=search_form.category.data, search=search_form.search.data))
    else:
        # We parse the query string to return the proper elements
        search_query = f"SELECT * FROM full_transcript_view;"
        category = request.args.get("category")
        search_string = request.args.get("search")
        if category == "title":
            search_query = f"SELECT * FROM full_transcript_view WHERE title ILIKE \'%{search_string}%\'"
        elif category == "keyword":
            search_query = f"SELECT * FROM full_transcript_view WHERE keyword=\'{search_string}\'"
        elif category == "content":
            search_query = f"SELECT * FROM full_transcript_view WHERE text_content ILIKE \'%{search_string}%\'"
        elif category == "summary":
            search_query = f"SELECT * FROM full_transcript_view WHERE summary ILIKE \'%{search_string}%\'"
        elif category == "location":
            search_query = f"SELECT * FROM full_transcript_view WHERE street_name ILIKE \'%{search_string}%\'"
        elif category == "participants":
            search_query = f"SELECT * FROM full_transcript_view WHERE name ILIKE \'%{search_string}%\'"
        

        # After retrieving the transcripts, we parse them into dictionarys to be sent back to the main screen
        transcripts_res = FullTranscript.run_and_return_many(conn, search_query)
        transcripts_res = convert_full_transcripts_to_json(transcripts_res)
        transcripts_res = check_if_parsed_transcripts_are_bookmarked(current_user.user_id, transcripts_res, conn)

        return render_template("transcripts/search.html", title="Search", form=search_form, loggedin=current_user.is_authenticated, email=current_user.email, data=transcripts_res)

# Displays a single transcript
@login_required
@transcripts.route("/<id>")
def view(id):
    # Retrieve all the transcripts with the relevant information, then convert
    transcripts_objs = FullTranscript.run_and_return_many(conn, f"SELECT * FROM full_transcript_view WHERE transcript_id={id};")
    transcripts_res = convert_full_transcripts_to_json(transcripts_objs)

    # We grab the single element and add the paths
    res = transcripts_res[0]
    res['audio_file_path'] = transcripts_objs[0].audio_file_path
    res['text_file_path'] = transcripts_objs[0].text_file_path
    return render_template("transcripts/view.html", data=res, title="View", loggedin=current_user.is_authenticated, email=current_user.email)

# Toggle a bookmarked transcript
@transcripts.route("/bookmark", methods=["POST"])
def bookmark():
    # Grab the ID
    id = request.form["id"]

    # If we have an id, start handling the transaction
    if id != None:
        _, res = conn.execute_and_return(f"SELECT COUNT(transcript_id) FROM bookmarks WHERE user_id={current_user.user_id} AND transcript_id={id};")
        # If a bookmark exists for this user, remove it
        if res[0][0] > 0:
            conn.execute(f"DELETE FROM bookmarks WHERE transcript_id={id};")
            return Response("Removed", status=200)
        # If it doesn't, we make one
        conn.execute(f"INSERT INTO bookmarks VALUES ({current_user.user_id}, {id});")
        return Response("Bookmarked", status=200)
    current_app.logger.info("id not found")
    return Response("ID not given", status=500)

# Download a pdf transcript
@transcripts.route("/download/text/<filename>")
def text(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)