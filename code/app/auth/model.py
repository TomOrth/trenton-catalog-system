
"""
This represents the User model for the users table

By: Tom Orth
"""
from app.database.entity import Entity
from flask_login import UserMixin

class User(Entity, UserMixin):
    """
    User model that extends from 2 class:
      - Entity for the database connection
      - UserMixin so that flask-login can be used
    """
    def __init__(self, user_id=-1, email="", password_hash="", lflag=""):
        """
        Constructs the entity
        """
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.lflag = lflag
    
    def get_id(self):
        """
        Returns the user_id for the login
        """
        return self.user_id
    
    @staticmethod
    def run_and_return(conn, query):
        """
        Run the given query on a connection object and create a single User
        """
        columns, content = conn.execute_and_return(query)
        user = User()
        return User.translate(user, columns, content[0])

    @staticmethod
    def run_and_return_many(conn, query):
        """
        We do not need to return many user objects so this is left unimplemented
        """
        pass

    @staticmethod
    def translate(obj, columns, content):
        """
        Translates tuples into a User object
        """
        return super(User, User).translate(obj, columns, content)
    
    @staticmethod
    def translate_many(obj, columns, contents):
        """
        We do not need to return many user objects so this is left unimplemented
        """
        pass