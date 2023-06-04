import cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

class MercadoLivreDB:
    def __init__(self, secure_bundle_path, client_id, client_secret):
        cloud_config = {
            'secure_connect_bundle': secure_bundle_path
        }
        auth_provider = PlainTextAuthProvider(client_id, client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect("MercadoLivreDB")
    
    def criar_tabela(self, tabela, colunas):
        colunas_str = ', '.join(colunas)
        query = f"CREATE TABLE IF NOT EXISTS {tabela} ({colunas_str});"
        self.session.execute(query)
    
    def inserir(self, tabela, valores):
        campos = ', '.join(valores.keys())
        placeholders = ', '.join(['%s'] * len(valores))
        query = f"INSERT INTO {tabela} ({campos}) VALUES ({placeholders});"
        self.session.execute(query, list(valores.values()))
    
    def buscar_por_id(self, tabela, id):
        query = f"SELECT * FROM {tabela} WHERE id = {id};"
        result = self.session.execute(query)
        return list(result)
    
    def listar_usuarios(self, tabela):
        query = f"SELECT * FROM {tabela};"
        result = self.session.execute(query)
        return list(result)
    
    def atualizar(self, tabela, id, campos, valores):
        for i in range(len(campos)):
            if isinstance(valores[i], str):
                valores[i] = "'" + valores[i] + "'"
            query = f"UPDATE {tabela} SET {campos[i]} = {valores[i]} WHERE id = {id};"
            self.session.execute(query)
    
    def deletar(self, tabela, id):
        query = f"DELETE FROM {tabela} WHERE id = {id};"
        self.session.execute(query)


# Função para inserir um usuário manualmente
def inserir_usuario_manual():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")

    usuario_id = uuid.uuid4()
    usuario_valores = {'id': usuario_id, 'nome': nome, 'email': email}
    db.inserir('usuario', usuario_valores)
    print("Usuário inserido com sucesso!")


# Função para listar todos os usuários
def listar_usuarios():
    usuarios = db.listar_usuarios('usuario')
    print("Lista de Usuários:")
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")


# Função para pesquisar um usuário por ID
def pesquisar_usuario():
    id = input("Digite o ID do usuário: ")
    usuario = db.buscar_por_id('usuario', id)
    if usuario:
        print(f"ID: {usuario[0].id}, Nome: {usuario[0].nome}, Email: {usuario[0].email}")
    else:
        print("Usuário não encontrado.")


# Função para alterar os dados de um usuário
def alterar_usuario():
    id = input("Digite o ID do usuário: ")
    nome = input("Digite o novo nome do usuário: ")
    email = input("Digite o novo e-mail do usuário: ")
    
    campos = ['nome', 'email']
    valores = [nome, email]
    
    db.atualizar('usuario', id, campos, valores)
    print("Usuário atualizado com sucesso!")


# Função para deletar um usuário
def deletar_usuario():
    id = input("Digite o ID do usuário a ser deletado: ")
    db.deletar('usuario', id)
    print("Usuário deletado com sucesso!")


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
    print("3. Pesquisar um usuário por ID")
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
