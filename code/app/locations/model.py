"""
Location Entity to represent the locations table

By: Tom Orth
"""
from app.database.entity import Entity
class Location(Entity):
    """
    Location entity class
    """
    def __init__(self):
        """
        Constructor to build the object
        """
        self.location_id = -1
        self.street_name = ""
    
    @staticmethod
    def run_and_return(conn, query):
        """
        Method will run and create a Location object to be used by the application
        """
        columns, content = conn.execute_and_return(query)
        location = Location()
        return Location.translate(location, columns, content[0])

    @staticmethod
    def run_and_return_many(conn, query):
        """
        Method will run and create a list of Location objects
        """
        columns, content = conn.execute_and_return(query)
        locations = []
        for _ in range(len(content)):
            locations.append(Location())
        return Location.translate_many(locations, columns, content)

    @staticmethod
    def translate(obj, columns, content):
        """
        Internal method to handle translation of a tuple to object
        """
        return super(Location, Location).translate(obj, columns, content)
    
    @staticmethod
    def translate_many(obj, columns, contents):
        """
        Internal method to handle translation of a tuples to objects
        """
        return super(Location, Location).translate_many(obj, columns, contents)