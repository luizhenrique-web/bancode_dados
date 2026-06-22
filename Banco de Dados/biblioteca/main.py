from bancodados import conectar

from popularunidade import popularUnidade
from populareditora import popularEditora
from popularusuario import popularUsuario

def main():
    conexao = conectar()
    cursor = conexao.cursor()
    
    try:
        popularUnidade(cursor)
        popularEditora(cursor)
        popularUsuario(cursor)
        
        conexao.commit()
        
        print("Dados inseridos com sucesso!")
    except Exception as erro:
        conexao.rollback()
        print("Erro:", erro)
    finally:
     cursor.close()
     conexao.close()
    
main()