"""
Represents the Search Form for locations

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

class LocationForm(FlaskForm):
    """
    Class the represents the new keyword form
    """
    location = TextField("Location", [Required(message="Must provide location")])