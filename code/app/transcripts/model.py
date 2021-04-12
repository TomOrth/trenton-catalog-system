"""
FullTranscript model to represent the full_transcript_view

By: Tom Orth
"""
from app.database.entity import Entity
class FullTranscript(Entity):
    """
    FullTranscript Entity Class
    """
    def __init__(self):
        """
        Instantiate the object
        """
        self.p_id = -1
        self.k_id = -1
        self.location_id = -1
        self.transcript_id = 1
        self.title = ""
        self.text_content = ""
        self.audio_file_path = ""
        self.text_file_path = ""
        self.summary = ""
    
    @staticmethod
    def run_and_return(conn, query):
        """
        Method will run and create a FullTranscript object to be used by the application
        """
        columns, content = conn.execute_and_return(query)
        FullTranscript = FullTranscript()
        return FullTranscript.translate(FullTranscript, columns, content[0])

    @staticmethod
    def run_and_return_many(conn, query):
        """
        Method will run and create a list of FullTranscript objects
        """
        columns, content = conn.execute_and_return(query)
        transcripts = []
        for _ in range(len(content)):
            transcripts.append(FullTranscript())
        return FullTranscript.translate_many(transcripts, columns, content)

    @staticmethod
    def translate(obj, columns, content):
        """
        Internal method to handle translation of a tuple to object
        """
        return super(FullTranscript, FullTranscript).translate(obj, columns, content)
    
    @staticmethod
    def translate_many(obj, columns, contents):
        """
        Internal method to handle translation of a tuples to objects
        """
        return super(FullTranscript, FullTranscript).translate_many(obj, columns, contents)