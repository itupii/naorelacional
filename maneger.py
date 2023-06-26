from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

class MercadoLivreDB:
    def __init__(self, secure_bundle_path, client_id, client_secret):
        cloud_config = {'secure_connect_bundle': secure_bundle_path}
        auth_provider = PlainTextAuthProvider(client_id, client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect("MercadoLivreDB")

    def criar_tabela(self, nome_tabela, campos):
        self.session.execute(
            f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({', '.join(campos)});"
        )

    def inserir(self, id, nome, email):
        self.session.execute(
            """
            INSERT INTO usuario (id, nome, email)
            VALUES (%s, %s, %s)
            """,
            (id, nome, email)
        )

    def inserirVendedor (self, id, nome, sobrenome, loja):
        self.session.execute(
            """
            INSERT INTO vendedor (id, nome, sobrenome, loja)
            VALUES (%s, %s, %s, %s)
            """,
            (id, nome, sobrenome, loja)
        )




    def inserirCompra (self, id, nome, valor):
        self.session.execute(
            """
            INSERT INTO compra (id, nome, valor)
            VALUES (%s, %s, %s)
            """,
            (id, nome, valor)
        )

    def inserirFavorito (self, id, nome, produto):
        self.session.execute(
            """
            INSERT INTO favorito (id, nome, produto)
            VALUES (%s, %s, %s)
            """,
            (id, nome, produto)
        )

    def inserirProduto (self, id, nome, preco):
        self.session.execute(
            """
            INSERT INTO produto (id, nome, preco)
            VALUES (%s, %s, %s)
            """,
            (id, nome, preco)
        )

    def consultar(self, id):
        query = f"SELECT * FROM usuario WHERE id = {id}"
        rows = self.session.execute(query)
        for row in rows:
            print(f"ID: {row.id}, Nome: {row.nome}, Email: {row.email}")

    def consultarVendedor(self, id):
        query = f"SELECT * FROM vendedor WHERE id = {id}"
        rows = self.session.execute(query)
        for row in rows:
            print(f"ID: {row.id}, Nome: {row.nome}, Sobrenome: {row.sobrenome}, Loja: {row.loja}")


    def consultarCompra(self, id):
        query = f"SELECT * FROM compra WHERE id = {id}"
        rows = self.session.execute(query)
        for row in rows:
            print(f"ID: {row.id}, Nome: {row.nome}, Valor: {row.valor}")

    def consultarFavorito(self, id):
        query = f"SELECT * FROM favorito WHERE id = {id}"
        rows = self.session.execute(query)
        for row in rows:
            print(f"ID: {row.id}, Nome: {row.nome}, Produto: {row.produto}")

    def consultarProduto(self, id):
        query = f"SELECT * FROM produto WHERE id = {id}"
        rows = self.session.execute(query)
        for row in rows:
            print(f"ID: {row.id}, Nome: {row.nome}, Preço: {row.preco}")


    def atualizar(self, id, campos, valor):
        query = f"UPDATE usuario SET {', '.join([f'{campo} = %s' for campo in campos])} WHERE id = {id}"
        self.session.execute(query, valor)

    

    def atualizarVendedor(self, id, campos, valor):
        query = f"UPDATE vendedor SET {', '.join([f'{campo} = %s' for campo in campos])} WHERE id = {id}"
        self.session.execute(query, valor)




    def atualizarCompra(self, id, campos, valor):
        query = f"UPDATE compra SET {', '.join([f'{campo} = %s' for campo in campos])} WHERE id = {id}"
        self.session.execute(query, valor)    

    def atualizarFavorito(self, id, campos, valor):
        query = f"UPDATE favorito SET {', '.join([f'{campo} = %s' for campo in campos])} WHERE id = {id}"
        self.session.execute(query, valor)

    def atualizarProduto(self, id, campos, valor):
        query = f"UPDATE produto SET {', '.join([f'{campo} = %s' for campo in campos])} WHERE id = {id}"
        self.session.execute(query, valor)



    def deletar(self, id):
        query = f"DELETE FROM usuario WHERE id = {id}"
        self.session.execute(query)

    def deletarVendedor(self, id):
        query = f"DELETE FROM vendedor WHERE id = {id}"
        self.session.execute(query)


    def deletarCompra(self, id):
        query = f"DELETE FROM compra WHERE id = {id}"
        self.session.execute(query)

    def deletarFavorito(self, id):
        query = f"DELETE FROM favorito WHERE id = {id}"
        self.session.execute(query)


    def deletarProduto(self, id):
        query = f"DELETE FROM produto WHERE id = {id}"
        self.session.execute(query)


    

    def fechar(self):
        self.session.shutdown()
        self.session.cluster.shutdown()

if __name__ == "__main__":
    secure_bundle_path = "./secure-connect-mercadolivredb.zip"
    client_id = "BuBEchYmSlumjBjbjeaElsOy"
    client_secret = "Q_jJOR8Dv9Rm7QPwJBc1zp9RfpTLqgKk9eGO0m_f.FcfR,nFmFSjUrBqbr7+L6EZnSoOxO6Qyj_Dg39SQXv-ivfZq4wPvw7Wg0wljsn.ovKtU.O5Zx7zgmDo9KQXw0_0"

    db = MercadoLivreDB(secure_bundle_path, client_id, client_secret)

    def inserir_usuario():
        id = uuid.uuid4()
        print("ID do usuário: ", id)
        nome = input("Digite o nome: ")
        email = input("Digite o e-mail: ")
        db.inserir(id, nome, email)
        print("Usuário inserido com sucesso!")

    def consultar_usuario():
        id = str(input("Digite o ID do usuário: "))
        db.consultar(id)


    def atualizar_usuario():
        id = str(input("Digite o ID do usuário: "))
        nome = input("Digite o nome: ")
        email = input("Digite o e-mail: ")
        campos = ['nome', 'email']
        valores = [nome, email]
        db.atualizar(id, campos, valores)
        print("Usuário atualizado com sucesso!")


    def deletar_usuario():
        id = str(input("Digite o ID do usuário: "))
        db.deletar(id)
        print("Usuário deletado com sucesso!")



    def inserir_Vendedor():
        id = uuid.uuid4()
        print("ID do vendedor: ", id)
    
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        loja = input("Digite o nome da loja: ")
        db.inserirVendedor(id, nome, sobrenome, loja)   
        print("Vendedor inserido com sucesso!")
    


    def consultar_Vendedor():
        id = str(input("Digite o id: "))
        db.consultarVendedor(id)

    def atualizar_Vendedor():
        id = str(input("Digite o id: "))
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        loja = input("Digite o nome da loja: ")
        campos = ['nome','sobrenome',  'loja']
        valores = [nome, sobrenome,   loja]
        db.atualizarVendedor(id, campos, valores)
        print("Vendedor atualizado com sucesso!")

    

    def deletar_Vendedor():
        id = str(input("Digite o id: "))
        db.deletarVendedor(id)
        print("Vendedor deletado com sucesso!")



    def inserir_Compra():
        id = uuid.uuid4()
        print ("ID da compra: ", id)
        nome = input("Digite o nome: ")
        valor = float(input("Digite o valor: "))
        db.inserirCompra(id, nome, valor)
        print("Compra inserida com sucesso!")


    def consultar_Compra():
        id = str(input("Digite o id: "))
        db.consultarCompra(id)
        print("Compra encontrada com sucesso!")

    def atualizar_Compra():
        id = str(input("Digite o id: "))
        nome = input("Digite o nome: ")
        valor = float(input("Digite o valor: "))
        campos = ['nome', 'valor']
        valores = [nome, valor]
        db.atualizarCompra(id, campos, valores)
        print("Compra atualizada com sucesso!")

    def deletar_Compra():
        id = str(input("Digite o id: "))
        db.deletarCompra(id)
        print("Compra deletada com sucesso!")

    def inserir_favoritoCLI():
        id = uuid.uuid4()
        print ("ID do favorito: ", id)
        nome = input("Digite o nome: ")
        produto = input("Digite o nome do produto: ")
        db.inserirFavorito(id, nome, produto)
        print("Favorito inserido com sucesso!")



    def consultar_favoritoCLI():
        id = str(input("Digite o id: "))
        db.consultarFavorito(id)
        print("Favorito encontrado com sucesso!")

    

    def atualizar_FavoritoCLI():
        id = str(input("Digite o id: "))
        nome = input("Digite o nome: ")
        produto = input("Digite o nome do produto: ")
        campos = ['nome', 'produto']
        valor = [nome, produto]
        db.atualizarFavorito(id, campos, valor)
        print("Favorito atualizado com sucesso!")
        

    def deletar_FavoritoCLI():
        id = str(input("Digite o id: "))
        db.deletarFavorito(id)
        print("Favorito deletado com sucesso!")

    def inserir_Produto():
        id = uuid.uuid4()
        print ("ID do produto: ", id)
        nome = input("Digite o nome: ")
        preco = float(input("Digite o preço: "))
        db.inserirProduto(id, nome, preco)
        print("Produto inserido com sucesso!")


    def consultar_Produto():

        id = str(input("Digite o id: "))
        db.consultarProduto(id)
        print("Produto encontrado com sucesso!")

    def atualizar_Produto():

        id = str(input("Digite o id: "))
        nome = input("Digite o nome: ")
        preco = float(input("Digite o preço: "))
        campos = ['nome', 'preco']
        valor = [nome, preco]
        db.atualizarProduto(id, campos, valor)
        print("Produto atualizado com sucesso!")

    def deletar_Produto():
            
            id = str(input("Digite o id: "))
            db.deletarProduto(id)
            print("Produto deletado com sucesso!")  
        

# Configurações de autenticação e conexão
secure_bundle_path = './secure-connect-mercadolivredb.zip'
client_id = 'BuBEchYmSlumjBjbjeaElsOy'
client_secret = 'Q_jJOR8Dv9Rm7QPwJBc1zp9RfpTLqgKk9eGO0m_f.FcfR,nFmFSjUrBqbr7+L6EZnSoOxO6Qyj_Dg39SQXv-ivfZq4wPvw7Wg0wljsn.ovKtU.O5Zx7zgmDo9KQXw0_0'

# Criação da instância do banco de dados
db = MercadoLivreDB(secure_bundle_path, client_id, client_secret)
db.criar_tabela('usuario', ['id UUID PRIMARY KEY', 'nome TEXT', 'email TEXT'])
db.criar_tabela('vendedor', ['id UUID PRIMARY KEY', 'nome TEXT', 'sobrenome TEXT', 'loja TEXT'])
db.criar_tabela('compra', ['id UUID PRIMARY KEY', 'nome TEXT', 'valor FLOAT'])
db.criar_tabela('favorito', ['id UUID PRIMARY KEY', 'nome TEXT', 'produto TEXT'])
db.criar_tabela('produto', ['id UUID PRIMARY KEY', 'nome TEXT', 'preco FLOAT'])


# Menu principal
while True:
    print("Bem-vindo ao Mercado Livre!")
    print("1 - Usuário")
    print("2 - Vendedor")
    print("3 - Compra")
    print("4 - Favorito")
    print ("5 - Produto")
    print("0 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print("1 - Inserir")
        print("2 - Consultar")
        print("3 - Alterar")
        print("4 - Deletar")
        print("0 - Voltar")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            inserir_usuario()
        elif opcao == 2:
            consultar_usuario()
        elif opcao == 3:
            atualizar_usuario()
        elif opcao == 4:
            deletar_usuario()
        elif opcao == 0:
            continue
        else:
            print("Opção inválida.")
    elif opcao == 2:
        print("1 - Inserir")
        print("2 - Consultar")
        print("3 - Alterar")
        print("4 - Deletar")
        print("0 - Voltar")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            inserir_Vendedor()
        elif opcao == 2:
            consultar_Vendedor()
        elif opcao == 3:
            atualizar_Vendedor()
        elif opcao == 4:
            deletar_Vendedor()
        elif opcao == 0:
            continue
        else:
            print("Opção inválida.")
    elif opcao == 3:
        print("1 - Inserir")
        print("2 - Consultar")
        print("3 - Alterar")
        print("4 - Deletar")
        print("0 - Voltar")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            inserir_Compra()
        elif opcao == 2:
            consultar_Compra()
        elif opcao == 3:
            atualizar_Compra()
        elif opcao == 4:
            deletar_Compra()
        elif opcao == 0:
            continue
        else:
            print("Opção inválida.")

    elif opcao == 4:
        print("1 - Inserir")
        print("2 - Consultar")
        print("3 - Alterar")
        print("4 - Deletar")
        print("0 - Voltar")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            inserir_favoritoCLI()
        elif opcao == 2:
            consultar_favoritoCLI()
        elif opcao == 3:
            atualizar_FavoritoCLI()
        elif opcao == 4:
            deletar_FavoritoCLI()
        elif opcao == 0:
            continue
        else:
            print("Opção inválida.")

    elif opcao == 5:
        print("1 - Inserir")
        print("2 - Consultar")
        print("3 - Alterar")
        print("4 - Deletar")
        print("0 - Voltar")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            inserir_Produto()
        elif opcao == 2:
            consultar_Produto()
        elif opcao == 3:
            atualizar_Produto()
        elif opcao == 4:
            deletar_Produto()
        elif opcao == 0:
            continue
        else:
            print("Opção inválida.")
            
        
    elif opcao == 0:
        break






