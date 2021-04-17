"""
Represents the Search Form for keywords

By: Matthew Van Soelen
"""
from flask_wtf import FlaskForm

# Import Form elements
from wtforms import TextField, SelectField

# Import Form validators
from wtforms.validators import Required


class SearchForm(FlaskForm):
    """
    Class that represents the search form
    """
    search = TextField("Search")

class KeywordForm(FlaskForm):
    """
    Class the represents the new keyword form
    """
    keyword = TextField("Keyword", [Required(message="Must provide keyword")])