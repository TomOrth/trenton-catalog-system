"""
Controller for the transcripts (full info)

By: Tom Orth
"""

from app.bookmarks.model import BookmarkTranscript
from app.utils import convert_full_transcripts_to_json, check_if_parsed_transcripts_are_bookmarked
from app.bookmarks.form import SearchForm
from app.setup import conn
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash, Response, send_from_directory
from flask_login import login_required, current_user


bookmarks = Blueprint("bookmarks", __name__, url_prefix="/bookmarks")

# Search page for transcripts
@bookmarks.route("/list", methods=["GET", "POST"])
@login_required
def list():
    search_form = SearchForm(request.form) # Search Form
    if request.method == "POST" and search_form.validate_on_submit: # If POST request, we redirect to GET but with query string
        return redirect(url_for("bookmarks.list", category=search_form.category.data, search=search_form.search.data))
    else:
        # We parse the query string to return the proper elements
        search_query = f"SELECT * FROM user_transcript_view WHERE user_id={current_user.user_id};"
        category = request.args.get("category")
        search_string = request.args.get("search")
        if category == "title":
            search_query = f"SELECT * FROM user_transcript_view WHERE user_id={current_user.user_id} AND title ILIKE \'%{search_string}%\'"
        elif category == "content":
            search_query = f"SELECT * FROM user_transcript_view WHERE user_id={current_user.user_id} AND text_content ILIKE \'%{search_string}%\'"
        elif category == "summary":
            search_query = f"SELECT * FROM user_transcript_view WHERE user_id={current_user.user_id} AND summary ILIKE \'%{search_string}%\'"   

        # After retrieving the transcripts, we parse them into dictionarys to be sent back to the main screen
        transcripts_res = BookmarkTranscript.run_and_return_many(conn, search_query)
        transcripts_dicts = [transcript.__dict__ for transcript in transcripts_res]
        for i, transcript in transcripts_dicts:
            del transcript["password_hash"]
            del transcript["user_id"]
            transcripts_dicts[i] = transcript
        return render_template("bookmarks/list.html", title="Bookmarks", form=search_form, loggedin=current_user.is_authenticated, email=current_user.email, data=transcripts_dicts)
