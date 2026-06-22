from faker import Faker

faker = Faker("pt_BR")

def popularUsuario(cursor):
    for i in range(50):
        carteira = faker.random_number(digits=13, fix_len=True)
        nome = faker.name()
        endereco = faker.address()
        telefone = faker.phone_number()
        cursor.execute("""INSERT INTO usuario (numero_carteira, nome, endereco, telefone) VALUES (%s, %s, %s, %s)""",
        (carteira, nome, endereco, telefone))
        
    print("Usuários cadastrados com sucesso!")