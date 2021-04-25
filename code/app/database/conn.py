"""
This contains information related  to the database connection. By having a super class, we can abstract out 
the database connections to allow for different sources.

By: Tom Orth
"""
import psycopg2

class Connection(object):
    """
    Super class for all database connections
    All methods need to be extended in the subclasses
    """
    def __init__(self, config):
        """
        Construct a Connection object with a given config
        """
        self.config = config # The config for the object
        self.conn = None # The underlying object that represents the driver's connection object
        self.is_connected = False # Tells whether or not the database is connected

    def connect(self):
        """
        This method will instantiate a database connection for a given request
        """
        pass
    
    def disconnect(self):
        """
        This method will disconnect a database connection after a request
        """
        pass
    
    def execute_and_return(self, query):
        """
        This method will execute a query and then return the results of columns and tuples
        """
        if not self.is_connected:
            self.connect()
    
    def execute(self, query):
        """
        This method will only execute a query and not return
        """
        if not self.is_connected:
            self.connect()
    
    def rollback(self):
        """
        Rollback a failed transaction
        """
        pass

class PostgresConnection(Connection):
    """
    Postgres Connection object using psycopg2
    """

    def __init__(self, config):
        """
        Calls the super constructor to setup the object
        """
        super().__init__(config)
    
    def connect(self):
        """
        Setup a new database connection with psycopg2
        """
        self.conn = psycopg2.connect(dbname=self.config["db"], user=self.config["user"], password=self.config["password"])
        self.is_connected = True

    def disconnect(self):
        """
        Disconnects the psycopg2 connection
        """
        self.conn.close()
        self.is_connected = False
    
    def execute(self, query):
        """
        Only execute the SQL query to postgres
        """
        super().execute(query)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        cur.close()
        self.disconnect()

    def execute_and_return(self, query):
        """
        Execute and return the columns and tuples that Postgres sends back in the form (string[], tuples[])
        """
        super().execute_and_return(query)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        content = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        return columns, content
    
    def rollback(self):
        """
        Rollback transaction
        """
        self.conn.rollback()
        self.is_connected = False