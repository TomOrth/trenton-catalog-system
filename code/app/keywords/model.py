from database.entity import Entity
class Keyword(Entity):
    def __init__(self):
        self.k_id = -1
        self.keyword = ""
    
    @staticmethod
    def run_and_return(conn, query):
        columns, content = conn.execute_and_return(query)
        keyword = Keyword()
        return Keyword.translate(keyword, columns, content[0])

    @staticmethod
    def run_and_return_many(conn, query):
        columns, content = conn.execute_and_return(query)
        keywords = []
        for _ in range(len(content)):
            keywords.append(Keyword())
        return Keyword.translate_many(keywords, columns, content)

    @staticmethod
    def translate(obj, columns, content):
        return super(Keyword, Keyword).translate(obj, columns, content)
    
    @staticmethod
    def translate_many(obj, columns, contents):
        return super(Keyword, Keyword).translate_many(obj, columns, contents)