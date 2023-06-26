from py2neo import Graph, Node

# Conexão com o banco de dados Neo4j
graph = Graph("neo4j+s://9e04d591.databases.neo4j.io", auth=("neo4j", "vxcxh7Zg7FjOoP5DSfo6oIC6x5-aVlKOTsHOipNSmbY"))

# Função para inserir um nó em uma coleção
def insert_node(collection, properties):
    node = Node(collection, **properties)
    graph.create(node)

# Função para atualizar um nó em uma coleção
def update_node(collection, node_id, properties):
    node = graph.nodes.match(collection, id=node_id).first()
    if node:
        for key, value in properties.items():
            node[key] = value
        graph.push(node)

# Função para pesquisar nós em uma coleção
def search_nodes(collection, properties):
    query = f"MATCH (node:{collection})"
    if properties:
        query += " WHERE "
        conditions = []
        for key, value in properties.items():
            conditions.append(f"node.{key} = '{value}'")
        query += " AND ".join(conditions)
    query += " RETURN node"
    result = graph.run(query)
    return result

# Função para excluir um nó em uma coleção
def delete_node(collection, node_id):
    graph.run(f"MATCH (node:{collection} {{id: '{node_id}'}}) DELETE node")

# Função para listar todos os nós de uma coleção
def list_nodes(collection):
    result = graph.run(f"MATCH (node:{collection}) RETURN node")
    for record in result:
        print(record["node"])

# Função para inserir informações manualmente
def insert_manual():
    collection = input("Informe a coleção (Usuário, Vendedor, Produto, Compra): ")
    properties = {}
    while True:
        key = input("Informe o nome da propriedade (ou deixe em branco para finalizar): ")
        if not key:
            break
        value = input(f"Informe o valor para a propriedade '{key}': ")
        properties[key] = value
    insert_node(collection, properties)

# Função para atualizar informações manualmente
def update_manual():
    collection = input("Informe a coleção (Usuário, Vendedor, Produto, Compra): ")
    node_id = input("Informe o ID do nó a ser atualizado: ")
    properties = {}
    while True:
        key = input("Informe o nome da propriedade (ou deixe em branco para finalizar): ")
        if not key:
            break
        value = input(f"Informe o novo valor para a propriedade '{key}': ")
        properties[key] = value
    update_node(collection, node_id, properties)

# Função para deletar todos os nós de uma coleção
def delete_all_nodes(collection):
    graph.run(f"MATCH (node:{collection}) DELETE node")

# Função para adicionar um nó aos favoritos
def add_to_favorites():
    collection = input("Informe a coleção (Usuário, Vendedor, Produto, Compra): ")
    node_id = input("Informe o ID do nó a ser adicionado aos favoritos: ")
    favorite_node_id = input("Informe o ID do nó favorito: ")
    properties = {
        "favorite_of": favorite_node_id
    }
    update_node(collection, node_id, properties)
    print("Nó adicionado aos favoritos com sucesso.")


 # função para criar qualquer tipo de nó
def create_node(collection, properties):
    node = Node(collection, **properties)
    graph.create(node)


# Loop principal
while True:
    print("\n=== MENU ===")
    print("1. Listar clientes")
    print("2. Listar produtos")
    print("3. Listar compras")
    print("4. Listar vendedores")
    print("5- Listar favoritos de um cliente")
    print("6- Inserir informações manualmente")
    print("7- Atualizar informações manualmente")
    print("8- criar um nó")
    print("9- Deletar todos os nós de uma coleção")
    print("10- Adicionar nó aos favoritos")


    print("11. Sair")

    choice = input("Escolha uma opção: ")

    if choice == "1":
        print("\n=== CLIENTES ===")
        list_nodes("Usuário")
    elif choice == "2":
        print("\n=== PRODUTOS ===")
        list_nodes("Produto")
    elif choice == "3":
        print("\n=== COMPRAS ===")
        list_nodes("Compra")
    elif choice == "4":
        print("\n=== VENDEDORES ===")
        list_nodes("Vendedor")

    elif choice == "5":
        print("\n=== FAVORITOS ===")
        list_nodes("Favorito")
    elif choice == "6":
        print("\n=== INSERIR INFORMAÇÕES MANUALMENTE ===")
        insert_manual()
    elif choice == "7":
        print("\n=== ATUALIZAR INFORMAÇÕES MANUALMENTE ===")
        update_manual()
    elif choice == "8":
        print("\n=== CRIAR NÓ ===")
        collection = input("Informe a coleção : ")
        properties = {}
        while True:
            key = input("Informe o nome da propriedade (ou deixe em branco para finalizar): ")
            if not key:
                break
            value = input(f"Informe o valor para a propriedade '{key}': ")
            properties[key] = value
        create_node(collection, properties)

    elif choice == "9":
        collection = input("Informe a coleção a ser deletada (Usuário, Vendedor, Produto, Compra, Favorito): ")
        delete_all_nodes(collection)
        print(f"Todos os nós da coleção {collection} foram deletados.")
    elif choice == "10":
        print("\n=== ADICIONAR NÓ AOS FAVORITOS ===")
        add_to_favorites()
    elif choice == "11":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

    continue_option = input("Pressione 'Enter' para voltar ao menu ou digite 's' para sair: ")
    if continue_option.lower() == "s":
        break

