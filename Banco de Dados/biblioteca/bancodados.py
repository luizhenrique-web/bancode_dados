import psycopg2

def conectar():
    conexao = psycopg2.connect(
        host="localhost",
        dbname="biblioteca",
        user="postgres",
        password="1234",
        port="5432"
    )
    return conexao