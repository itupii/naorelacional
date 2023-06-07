import cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

class MercadoLivreDB:
    def __init__(self, secure_bundle_path, client_id, client_secret):
        cloud_config = {'secure_connect_bundle': secure_bundle_path}
        auth_provider = PlainTextAuthProvider(client_id, client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect("MercadoLivreDB")

    def criar_tabela(self, tabela, colunas):
        colunas_str = ', '.join(colunas)
        query = f"CREATE TABLE IF NOT EXISTS {tabela} ({colunas_str});"
        self.session.execute(query)

        # Criar índice secundário para a coluna 'email'
        index_query = f"CREATE INDEX IF NOT EXISTS idx_{tabela}_email ON {tabela} (email);"
        self.session.execute(index_query)

    def inserir(self, tabela, valores):
        query = f"INSERT INTO {tabela} JSON %s;"
        self.session.execute(query, [cassandra.util.json.dumps(valores)])

    def buscar_por_email(self, tabela, email):
        query = f"SELECT * FROM {tabela} WHERE email = %s;"
        result = self.session.execute(query, [email])
        return list(result)

    def listar_usuarios(self, tabela):
        query = f"SELECT * FROM {tabela};"
        result = self.session.execute(query)
        return list(result)

    def atualizar(self, tabela, email, campos, valores):
        id_query = f"SELECT id FROM {tabela} WHERE email = %s;"
        id_result = self.session.execute(id_query, [email])
        user_id = id_result[0].id if id_result else None

        if user_id:
            set_clause = ', '.join([f"{campo} = %s" for campo in campos])
            query = f"UPDATE {tabela} SET {set_clause} WHERE id = %s;"
            self.session.execute(query, valores + [user_id])

    def deletar(self, tabela, email):
        query = f"DELETE FROM {tabela} WHERE email = %s;"
        self.session.execute(query, [email])




# Função para inserir um usuário manualmente
def inserir_usuario_manual():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")

    usuario_valores = {'nome': nome, 'email': email}
    db.inserir('usuario', usuario_valores)
    print("Usuário inserido com sucesso!")


# Função para listar todos os usuários
def listar_usuarios():
    usuarios = db.listar_usuarios('usuario')
    print("Lista de Usuários:")
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")


# Função para pesquisar um usuário por e-mail
def pesquisar_usuario():
    email = input("Digite o e-mail do usuário: ")
    usuario = db.buscar_por_email('usuario', email)
    if usuario:
        print(f"ID: {usuario[0].id}, Nome: {usuario[0].nome}, Email: {usuario[0].email}")
    else:
        print("Usuário não encontrado.")


# Função para alterar os dados de um usuário
def alterar_usuario():
    email = input("Digite o e-mail do usuário: ")
    usuario = db.buscar_por_email('usuario', email)
    if usuario:
        id = usuario[0].id
        nome = input("Digite o novo nome do usuário: ")
        novo_email = input("Digite o novo e-mail do usuário: ")
        campos = ['nome', 'email']
        valores = [nome, novo_email]

        db.atualizar('usuario', email, campos, valores)
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")


# Função para deletar um usuário
def deletar_usuario():
    email = input("Digite o e-mail do usuário a ser deletado: ")
    usuario = db.buscar_por_email('usuario', email)
    if usuario:
        db.deletar('usuario', email)
        print("Usuário deletado com sucesso!")
    else:
        print("Usuário não encontrado.")


# Configurações de autenticação e conexão
secure_bundle_path = './secure-connect-mercadolivredb.zip'
client_id = 'BuBEchYmSlumjBjbjeaElsOy'
client_secret = 'Q_jJOR8Dv9Rm7QPwJBc1zp9RfpTLqgKk9eGO0m_f.FcfR,nFmFSjUrBqbr7+L6EZnSoOxO6Qyj_Dg39SQXv-ivfZq4wPvw7Wg0wljsn.ovKtU.O5Zx7zgmDo9KQXw0_0'

# Criação da instância do banco de dados
db = MercadoLivreDB(secure_bundle_path, client_id, client_secret)
db.criar_tabela('usuario', ['id UUID PRIMARY KEY', 'nome TEXT', 'email TEXT'])

# Loop para realizar operações com usuários
while True:
    print("\nO que você deseja fazer?")
    print("1. Inserir um novo usuário")
    print("2. Listar todos os usuários")
    print("3. Pesquisar um usuário por e-mail")
    print("4. Alterar os dados de um usuário")
    print("5. Deletar um usuário")
    print("6. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        inserir_usuario_manual()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        pesquisar_usuario()
    elif opcao == "4":
        alterar_usuario()
    elif opcao == "5":
        deletar_usuario()
    elif opcao == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")
    
    opcao_continuar = input("Deseja voltar ao menu principal? (s/n): ")
    if opcao_continuar.lower() != 's':
        break
