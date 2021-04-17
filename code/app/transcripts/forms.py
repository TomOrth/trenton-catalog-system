"""
Represents the Search Form for transcripts

By: Tom Orth
"""
from flask_wtf import FlaskForm

# Import Form elements
from wtforms import TextField, SelectField, SelectMultipleField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired

# Import Form validators
from wtforms.validators import Required


# Define the login form (WTForms)
class SearchForm(FlaskForm):
    """
    Class that represents the search form
    """
    search = TextField("Seach", [
                Required(message='Must provide a search query')])
    category = SelectField("Category", choices = ["participants", "location", "keyword", "title", "content", "summary"])


class TranscriptForm(FlaskForm):
    """
    Class the represents the new transcript form
    """
    title = TextField("Title", [Required(message="Must provide title")])
    summary = TextAreaField("Summary", [Required(message="Must provide summary")])
    audio_path = TextField("Audio File Path", [Required(message="Must provide audio path")])
    text_file = FileField("PDF File Upload")
    text_content = TextAreaField("Text Content", [Required()])
    participants = SelectMultipleField("Participants (Hold ctrl or command when selecting entries)", coerce=int)
    keywords = SelectMultipleField("Keywords  (Hold ctrl or command when selecting entries)", coerce=int)
    locations = SelectMultipleField("Locations  (Hold ctrl or command when selecting entries)", coerce=int)

class TranscriptUpdateForm(FlaskForm):
    """
    Class the represents updating the transcript
    """
    title = TextField("Title")
    summary = TextAreaField("Summary")
    audio_path = TextField("Audio File Path")
    text_file = FileField("PDF File Upload")
    text_content = TextAreaField("Text Content")
    
