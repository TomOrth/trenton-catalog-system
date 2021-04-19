"""
Controller for the transcripts (full info)

By: Tom Orth
"""

from app.transcripts.model import FullTranscript
from app.participants.model import Participant
from app.keywords.model import Keyword
from app.locations.model import Location
from app.utils import convert_full_transcripts_to_json, check_if_parsed_transcripts_are_bookmarked
from app.transcripts.forms import SearchForm, TranscriptForm, TranscriptUpdateForm
from app.setup import conn
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash, Response, send_from_directory
from flask_login import login_required, current_user
from wtforms.validators import Optional
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
import psycopg2
import os



transcripts = Blueprint("transcripts", __name__, url_prefix="/transcripts")

# Search page for transcripts
@transcripts.route("/search", methods=["GET", "POST"])
@login_required
def search():
    search_form = SearchForm(request.form) # Search Form
    if request.method == "POST" and search_form.validate_on_submit: # If POST request, we redirect to GET but with query string
        return redirect(url_for("transcripts.search", category=search_form.category.data, search=search_form.search.data))
    else:
        # We parse the query string to return the proper elements
        search_query = f"SELECT * FROM full_transcript_view;"
        category = request.args.get("category")
        # Were removing single quotes for parsing reasons
        search_string = request.args.get("search")
        if search_string != None:
            search_string = search_string.replace("'", "")
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

        return render_template("transcripts/search.html", title="Search", form=search_form, lflag=current_user.lflag, loggedin=current_user.is_authenticated, email=current_user.email, data=transcripts_res)

# Displays a single transcript
@transcripts.route("/<id>")
@login_required
def view(id):
    # Retrieve all the transcripts with the relevant information, then convert
    transcripts_objs = FullTranscript.run_and_return_many(conn, f"SELECT * FROM full_transcript_view WHERE transcript_id={id};")
    transcripts_res = convert_full_transcripts_to_json(transcripts_objs)

    # We grab the single element and add the paths
    res = transcripts_res[0]
    res['audio_file_path'] = transcripts_objs[0].audio_file_path
    res['text_file_path'] = transcripts_objs[0].text_file_path
    return render_template("transcripts/view.html", data=res, title="View", lflag=current_user.lflag, loggedin=current_user.is_authenticated, email=current_user.email)

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

@transcripts.route("/new", methods=["GET", "POST"])
@login_required
def new():
    form = TranscriptForm(CombinedMultiDict((request.files, request.form)))
    form.participants.choices = [(participant.p_id, participant.name) for participant in Participant.run_and_return_many(conn, f"SELECT * FROM participants;")]
    form.keywords.choices = [(keyword.k_id, keyword.keyword) for keyword in Keyword.run_and_return_many(conn, f"SELECT * FROM keywords;")]
    form.locations.choices = [(location.location_id, location.street_name) for location in Location.run_and_return_many(conn, f"SELECT * FROM locations;")]
    if request.method == "POST" and form.validate_on_submit():
        current_app.logger.info("fdafda")
        filename = secure_filename(form.text_file.data.filename)
        form.text_file.data.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        _, id_res = conn.execute_and_return(f"INSERT INTO transcripts(title, summary, text_file_path, audio_file_path, text_content) VALUES (\'{form.title.data}\', \'{form.summary.data}\', \'{filename}\', \'{form.audio_path.data}\', \'{form.text_content.data}\') RETURNING transcript_id;")
        id = id_res[0][0]
        for pid in form.participants.data:
            conn.execute(f"INSERT INTO participates VALUES ({pid}, {id});")
        for kid in form.keywords.data:
            conn.execute(f"INSERT INTO describes VALUES ({kid}, {id});")
        for lid in form.locations.data:
            conn.execute(f"INSERT INTO mentions VALUES ({lid}, {id});")
        return redirect(url_for("transcripts.search"))
    return render_template("transcripts/new.html", title="New Transcript", lflag=current_user.lflag, form=form, loggedin=current_user.is_authenticated, email=current_user.email)

@transcripts.route("/update", methods=["GET", "POST"])
@login_required
def update():
    id = request.args.get("id")
    transcript = FullTranscript.run_and_return(conn, f"SELECT DISTINCT transcript_id, title, summary, text_file_path, audio_file_path, text_content FROM full_transcript_view WHERE transcript_id={id};")
    form = TranscriptUpdateForm(CombinedMultiDict((request.files, request.form)))
    if request.method == "POST" and form.validate_on_submit():
        filename = transcript.text_file_path
        if form.text_file.data != None:
            os.remove(os.path.join(current_app.config["UPLOAD_FOLDER"], transcript.text_file_path))
            filename = secure_filename(form.text_file.data.filename)
            form.text_file.data.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        text_content = form.text_content.data.replace("'", "")
        conn.execute(f"UPDATE transcripts SET title=\'{form.title.data}\', summary=\'{form.summary.data}\', audio_file_path=\'{form.audio_path.data}\', text_file_path=\'{filename}\', text_content=\'{text_content}\' WHERE transcript_id={id};")
        return redirect(url_for("transcripts.search"))
    form.title.data = transcript.title
    form.summary.data = transcript.summary
    form.audio_path.data = transcript.audio_file_path
    form.text_content.data = transcript.text_content
    return render_template("transcripts/update.html", id=id, title="Update Transcript", lflag=current_user.lflag, form=form, loggedin=current_user.is_authenticated, email=current_user.email)

# Download a pdf transcript
@transcripts.route("/download/text/<filename>")
def text(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

# Delete a transcript
@transcripts.route("/delete", methods=["POST"])
def delete():
    id = request.form["id"]
    try:
        _, res = conn.execute_and_return(f"SELECT text_file_path FROM transcripts WHERE transcript_id={id};")
        path = res[0][0]
        os.remove(os.path.join(current_app.config["UPLOAD_FOLDER"], path))
        conn.execute(f"DELETE FROM participates WHERE transcript_id={id};")
        conn.execute(f"DELETE FROM describes WHERE transcript_id={id};")
        conn.execute(f"DELETE FROM mentions WHERE transcript_id={id};")
        conn.execute(f"DELETE FROM transcripts WHERE transcript_id={id};")

        return Response("Deleted", status=200)
    except psycopg2.OperationalError as e:
        return Response(f"Error: {e}", status=404)