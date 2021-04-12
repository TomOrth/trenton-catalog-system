"""
This superclass allows for abstraction of the tables

By: Tom Orth
"""
class Entity(object):

    """
    Superclass for all database models
    """
    @staticmethod
    def translate(obj, columns, content):
        """
        This method will take the columns from a Connection#execute_and_run and set the proper values for the instance variables
        """
        for col, item in zip(columns, content):
            setattr(obj, col, item)
        return obj
    
    @staticmethod
    def translate_many(objs, columns, contents):
        """
        Sets up many objects and sets the proper values for many returned tuples from Connection#execute_and_run
        """
        for i in range(len(objs)):
            objs[i] = Entity.translate(objs[i], columns, contents[i])
        return objs

    @staticmethod
    def run_and_return(conn, query):
        """
        Runs a query on a given Connection object to get a resulting Entity
        """
        pass
    
    @staticmethod
    def run_and_return_many(conn, query):
        """
        Runs a query on a given Connection object to get a list of resulting Entities
        """
        pass
