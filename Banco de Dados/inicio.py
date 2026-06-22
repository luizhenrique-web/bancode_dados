import psycopg2

conexao = psycopg2.connect(
    dbname="aula", user = "postgres", password = "1234", host = "localhost", port = "5432"
)

cursor = conexao.cursor()

if cursor:
    print("Conexão estabelecida com sucesso!")
else:
    print("Falha na conexão com o banco de dados.")