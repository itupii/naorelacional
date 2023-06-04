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

# Loop principal
while True:
    print("\n=== MENU ===")
    print("1. Listar clientes")
    print("2. Listar produtos")
    print("3. Listar compras")
    print("4. Inserir informações manualmente")
    print("5. Deletar um nó")
    print("6. Sair")

    choice = input("Escolha uma opção: ")
    
    if choice == "1":
        print("\n=== CLIENTES ===")
        list_nodes("Usuário")
        continue_option = input("Pressione 'Enter' para voltar ao menu ou digite 's' para sair: ")
        if continue_option.lower() == "s":
            break
    elif choice == "2":
        print("\n=== PRODUTOS ===")
        list_nodes("Produto")
        continue_option = input("Pressione 'Enter' para voltar ao menu ou digite 's' para sair: ")
        if continue_option.lower() == "s":
            break
    elif choice == "3":
        print("\n=== COMPRAS ===")
        list_nodes("Compra")
        continue_option = input("Pressione 'Enter' para voltar ao menu ou digite 's' para sair: ")
        if continue_option.lower() == "s":
            break
    elif choice == "4":
        print("\n=== INSERIR INFORMAÇÕES MANUALMENTE ===")
        insert_manual()
        continue_option = input("Pressione 'Enter' para voltar ao menu ou digite 's' para sair: ")
        if continue_option.lower() == "s":
            break
    elif choice == "5":
        node_id = input("Informe o ID do nó a ser deletado: ")
        delete_node("Usuário", node_id)
        delete_node("Vendedor", node_id)
        delete_node("Produto", node_id)
        delete_node("Compra", node_id)
        print("Nó deletado com sucesso.")
        continue_option = input("Pressione 'Enter' para voltar ao menu ou digite 's' para sair: ")
        if continue_option.lower() == "s":
            break
    elif choice == "6":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
