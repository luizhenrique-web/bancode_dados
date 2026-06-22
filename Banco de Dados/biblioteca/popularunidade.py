from faker import Faker

faker = Faker("pt_BR") 

def popularUnidade(cursor):
    for i in range(8):
        codigo = faker.random_number(digits=7, fix_len=True)
        nome = (f"Unidade Biblioteca {i+1}")
        endereco = faker.address()
        cursor.execute("""INSERT INTO unidade_biblioteca (codigo_unidade, nome_unidade, endereco) VALUES (%s, %s, %s)""",
        (codigo, nome, endereco))
    
    print("Unidades inseridas com sucesso!")