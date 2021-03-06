"""
Keyword model to represent the keywords table

By: Tom Orth
"""
from app.database.entity import Entity
class Keyword(Entity):
    """
    Keyword Entity Class
    """
    def __init__(self):
        """
        Instantiate the object
        """
        self.k_id = -1
        self.keyword = ""
    
    @staticmethod
    def run_and_return(conn, query):
        """
        Method will run and create a Keyword object to be used by the application
        """
        columns, content = conn.execute_and_return(query)
        keyword = Keyword()
        return Keyword.translate(keyword, columns, content[0])

    @staticmethod
    def run_and_return_many(conn, query):
        """
        Method will run and create a list of Keyword objects
        """
        columns, content = conn.execute_and_return(query)
        keywords = []
        for _ in range(len(content)):
            keywords.append(Keyword())
        return Keyword.translate_many(keywords, columns, content)

    @staticmethod
    def translate(obj, columns, content):
        """
        Internal method to handle translation of a tuple to object
        """
        return super(Keyword, Keyword).translate(obj, columns, content)
    
    @staticmethod
    def translate_many(obj, columns, contents):
        """
        Internal method to handle translation of a tuples to objects
        """
        return super(Keyword, Keyword).translate_many(obj, columns, contents)