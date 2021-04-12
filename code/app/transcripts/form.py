"""
Represents the Search Form for transcripts
"""
from flask_wtf import FlaskForm

# Import Form elements
from wtforms import TextField, SelectField

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
