from cassandra.cluster import Cluster

# Conectar ao cluster do Cassandra
cluster = Cluster(['localhost'])  # substitua 'localhost' pelo endereço do seu cluster
session = cluster.connect()

# Criação das keyspace e tabelas
session.execute("CREATE KEYSPACE IF NOT EXISTS mercado_livre WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}")
session.execute("USE mercado_livre")

session.execute("CREATE TABLE IF NOT EXISTS usuario (id UUID PRIMARY KEY, nome TEXT, email TEXT)")
session.execute("CREATE TABLE IF NOT EXISTS vendedor (id UUID PRIMARY KEY, nome TEXT, endereco TEXT)")
session.execute("CREATE TABLE IF NOT EXISTS produto (id UUID PRIMARY KEY, nome TEXT, preco DECIMAL)")
session.execute("CREATE TABLE IF NOT EXISTS compra (id UUID PRIMARY KEY, usuario_id UUID, vendedor_id UUID, produto_id UUID)")

# Função para inserir um registro em todas as coleções
def insert_data():
    # Inserir usuário
    session.execute("INSERT INTO usuario (id, nome, email) VALUES (uuid(), 'Usuário 1', 'usuario1@gmail.com')")

    # Inserir vendedor
    session.execute("INSERT INTO vendedor (id, nome, endereco) VALUES (uuid(), 'Vendedor 1', 'Rua A, 123')")

    # Inserir produto
    session.execute("INSERT INTO produto (id, nome, preco) VALUES (uuid(), 'Produto 1', 9.99)")

    # Inserir compra
    session.execute("INSERT INTO compra (id, usuario_id, vendedor_id, produto_id) VALUES (uuid(), (SELECT id FROM usuario WHERE nome = 'Usuário 1'), (SELECT id FROM vendedor WHERE nome = 'Vendedor 1'), (SELECT id FROM produto WHERE nome = 'Produto 1'))")

# Função para atualizar um registro em todas as coleções
def update_data():
    # Atualizar usuário
    session.execute("UPDATE usuario SET email = 'usuario1_atualizado@gmail.com' WHERE nome = 'Usuário 1'")

    # Atualizar vendedor
    session.execute("UPDATE vendedor SET endereco = 'Rua B, 456' WHERE nome = 'Vendedor 1'")

    # Atualizar produto
    session.execute("UPDATE produto SET preco = 19.99 WHERE nome = 'Produto 1'")

    # Atualizar compra
    session.execute("UPDATE compra SET vendedor_id = (SELECT id FROM vendedor WHERE nome = 'Vendedor 1'), produto_id = (SELECT id FROM produto WHERE nome = 'Produto 1') WHERE usuario_id = (SELECT id FROM usuario WHERE nome = 'Usuário 1')")

# Função para buscar registros em todas as coleções
def search_data():
    # Buscar usuários
    result = session.execute("SELECT * FROM usuario")
    for row in result:
        print(row.id, row.nome, row.email)

    # Buscar vendedores
    result = session.execute("SELECT * FROM vendedor")
    for row in result:
        print(row.id, row.nome, row.endereco)

    # Buscar produtos
    result = session.execute("SELECT * FROM produto")
    for row in result:
        print(row.id, row.nome, row.preco)

    # Buscar compras
    result = session.execute("SELECT * FROM compra")
    for row in result:
        print(row.id, row.usuario_id, row.vendedor_id, row.produto_id)

# Função para excluir registros em todas as coleções
def delete_data():
    # Excluir usuário
    session.execute("DELETE FROM usuario WHERE nome = 'Usuário 1'")

    # Excluir vendedor
    session.execute("DELETE FROM vendedor WHERE nome = 'Vendedor 1'")

    # Excluir produto
    session.execute("DELETE FROM produto WHERE nome = 'Produto 1'")

    # Excluir compra
    session.execute("DELETE FROM compra WHERE usuario_id = (SELECT id FROM usuario WHERE nome = 'Usuário 1')")

# Executar as operações
insert_data()
update_data()
search_data()
delete_data()

# Fechar a conexão com o cluster
session.shutdown()
cluster.shutdown()
