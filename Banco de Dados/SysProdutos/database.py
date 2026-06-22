import psycopg2

class Database:
    def __init__(self):
       self.host = "localhost"
       self.dbname = "estoque"
       self.user = "postgres"
       self.password = "1234"
       self.port = "5432"
       
    def conectar(self):
        return psycopg2.connect(
            host=self.host,
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            port=self.port
        )
        

