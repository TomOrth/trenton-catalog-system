"""
BookmarkTranscript model to represent the user_transcript_view

By: Tom Orth
"""
from app.database.entity import Entity
class BookmarkTranscript(Entity):
    """
    BookmarkTranscript Entity Class
    """
    def __init__(self):
        """
        Instantiate the object
        """
        self.user_id = -1
        self.transcript_id = 1
        self.title = ""
        self.text_content = ""
        self.audio_file_path = ""
        self.text_file_path = ""
        self.summary = ""
    
    @staticmethod
    def run_and_return(conn, query):
        """
        Method will run and create a BookmarkTranscript object to be used by the application
        """
        columns, content = conn.execute_and_return(query)
        bt = BookmarkTranscript()
        return BookmarkTranscript.translate(bt, columns, content[0])

    @staticmethod
    def run_and_return_many(conn, query):
        """
        Method will run and create a list of BookmarkTranscript objects
        """
        columns, content = conn.execute_and_return(query)
        transcripts = []
        for _ in range(len(content)):
            transcripts.append(BookmarkTranscript())
        return BookmarkTranscript.translate_many(transcripts, columns, content)

    @staticmethod
    def translate(obj, columns, content):
        """
        Internal method to handle translation of a tuple to object
        """
        return super(BookmarkTranscript, BookmarkTranscript).translate(obj, columns, content)
    
    @staticmethod
    def translate_many(obj, columns, contents):
        """
        Internal method to handle translation of a tuples to objects
        """
        return super(BookmarkTranscript, BookmarkTranscript).translate_many(obj, columns, contents)