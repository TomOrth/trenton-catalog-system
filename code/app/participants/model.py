"""
Participant Entity to represent the participants table

By: Tom Orth
"""
from app.database.entity import Entity
class Participant(Entity):
    """
    Participant entity class
    """
    def __init__(self):
        """
        Constructor to build the object
        """
        self.p_id = -1
        self.name = ""
    
    @staticmethod
    def run_and_return(conn, query):
        """
        Method will run and create a Participant object to be used by the application
        """
        columns, content = conn.execute_and_return(query)
        participant = Participant()
        return Participant.translate(participant, columns, content[0])

    @staticmethod
    def run_and_return_many(conn, query):
        """
        Method will run and create a list of Participant objects
        """
        columns, content = conn.execute_and_return(query)
        participants = []
        for _ in range(len(content)):
            participants.append(Location())
        return Participant.translate_many(participants, columns, content)

    @staticmethod
    def translate(obj, columns, content):
        """
        Internal method to handle translation of a tuple to object
        """
        return super(Participant, Participant).translate(obj, columns, content)
    
    @staticmethod
    def translate_many(obj, columns, contents):
        """
        Internal method to handle translation of a tuples to objects
        """
        return super(Participant, Participant).translate_many(obj, columns, contents)