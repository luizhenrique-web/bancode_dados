from produto import Produto

def menu():
    while True:
        print("\n=== Sys Estoque ===")
        print("1. Cadastrar Produto")
        print("0. Sair")

        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                nomeProduto = input("Nome do produto: ")
                precoProduto = float(input("Preço do produto: "))
                quantidade = int(input("Quantidade do produto: "))

                novoProduto = Produto(nomeProduto, precoProduto, quantidade)
                novoProduto.cadastrar()

            case 0:
                break
            
menu()