from faker import Faker

faker = Faker("pt_BR")

def popularEditora(cursor):
    for i in range(10):
        nome = faker.company()
        endereco = faker.address()
        telefone = faker.phone_number()
        cursor.execute("""INSERT INTO editora (nome, endereco, telefone) VALUES (%s, %s, %s)""",
        (nome, endereco, telefone))
    print("Editoras inseridas com sucesso!")