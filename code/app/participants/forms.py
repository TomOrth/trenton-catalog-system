# Create New Participant form for Participants.
# By: Justin Pabon

from flask_wtf import FlaskForm

# Import Form elements
from wtforms import TextField

# Import Form validators
from wtforms.validators import Required


# Define the login form (WTForms)

class SearchForm(FlaskForm):
    """
    Class that represents the search form
    """
    search = TextField("Search")

class NewForm(FlaskForm):
    """
    Class that represents the new form
    """
    name = TextField("Participant's Name", [
                Required(message='Must provide a name for the participant.')])
