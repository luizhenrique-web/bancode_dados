from database import Database

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def cadastrar(self):
        banco = Database()
        conexao = banco.conectar()
        
        cursor = conexao.cursor()
        
        sql = """
        INSERT INTO produtos (nome, preco, quantidade)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (self.nome, self.preco, self.quantidade))
        conexao.commit()
        cursor.close()
        
        conexao.close()
        print("Produto cadastrado com sucesso!")
        