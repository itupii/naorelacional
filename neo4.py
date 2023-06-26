from py2neo import Graph, Node

# Conexão com o banco de dados Neo4j
graph = Graph("neo4j+s://83fb1521.databases.neo4j.io", auth=("neo4j", "xwMIT3boYBgtXMOhHzRsjDMMsdL6DFd-uuiUWRvWkA8"))

print ( ' \n ---* BEM VINDO AO MERCADO LIVRE *---' )

print ( " \n *** Cadastro ***" )
print ( " \n 1 - Cadastrar usuario" )
print ( " \n 2 - Cadastrar produto" )
print ( " \n 3 - Cadastrar vendedor" )
print ( " \n 4 - Cadastrar favorito" )

print ( " \n *** Listagem de Dados ***" )
print ( " \n 5 - Listar usuario" )
print ( " \n 6 - Listar produto" )
print ( " \n 7 - Listar vendedor" )

print ( " \n *** Atualizar Dados ***" )
print ( " \n 8 - Atualizar dados de usuario" )
print ( " \n 9 - Atualizar dados de produto" )
print ( " \n 10 - Atualizar dados do vendedor" )

print ( " \n *** Deletar ***" )
print ( " \n 11 - Excluir usuario" )
print ( " \n 12 - Excluir produto" )
print ( " \n 13 - Deletar vendedor" )
print ( " \n 14 - Deletar Favoritos" )
print ( " \n 15 - Deletar relacao")

opcao  =  int ( input ( ' \n Digite o numero da opcao desejada: ' ))

#criar usuário
if opcao == 1:
    nome = input('Digite o nome do usuario: ')
    email = input('Digite o email do usuario: ')
    usuario = Node('Usuario', nome=nome, email=email)
    graph.create(usuario)
    print('Usuario cadastrado com sucesso!')

#criar produto
elif opcao == 2:
    nome = input('Digite o nome do produto: ')
    nomevendedor = input('Digite o nome do vendedor: ')
    nomeUsuario = input('Digite o nome do usuario: ')

    #verificar se usuario e vendedor existem
    consultar = """
        MATCH (n:Usuario {nome: $nome})
        RETURN n
        """
    resultado = graph.run(consultar, nome=nomeUsuario).data()
    if resultado == []:
        print('Usuario nao encontrado!')
        exit()
    consultar = """
        MATCH (n:Vendedor {nome: $nome})
        RETURN n
        """
    resultado = graph.run(consultar, nome=nomevendedor).data()
    if resultado == []:
        print('Vendedor nao encontrado!')
        exit()

    else :
        #criar a relação "VENDER" em que o vendedor vende para o usuario
        consultar = """
        MATCH (a:Vendedor),(b:Usuario)
        WHERE a.nome = $nomevendedor AND b.nome = $nomeUsuario
        CREATE (a)-[r:VENDER]->(b)
        RETURN type(r)
        """
    graph.run(consultar, nomevendedor=nomevendedor, nomeUsuario=nomeUsuario)
    print('Relacao VENDER criada com sucesso!')

#criar vendedor
elif opcao == 3:
    nome = input('Digite o nome do vendedor: ')
    email = input('Digite o email do vendedor: ')
    vendedor = Node('Vendedor', nome=nome, email=email)
    graph.create(vendedor)
    print('Vendedor cadastrado com sucesso!')   

#criar favorito
elif opcao == 4:
    nomeUsuario = input('Digite o nome do usuario: ')
    nomeProduto = input('Digite o nome do produto: ')

   #verificar se usuario e produto existem
    consultar = """
        MATCH (n:Usuario {nome: $nome})
        RETURN n
        """
    resultado = graph.run(consultar, nome=nomeUsuario).data()
    if resultado == []:
        print('Usuario nao encontrado!')
        exit()
    consultar = """
        MATCH (n:Produto {nome: $nome})
        RETURN n
        """
    resultado = graph.run(consultar, nome=nomeProduto).data()
    if resultado == []:
        print('Produto nao encontrado!')
        exit()

    else :
#criar a relacao "FAVORITO" entre usuario e produto
        consultar = """
        MATCH (a:Usuario),(b:Produto)
        WHERE a.nome = $nomeUsuario AND b.nome = $nomeProduto
        CREATE (a)-[r:FAVORITO]->(b)
        RETURN type(r)
        """
    graph.run(consultar, nomeUsuario=nomeUsuario, nomeProduto=nomeProduto)
    print('Favorito cadastrado com sucesso!')


    
    



#listar usuario
elif opcao == 5:
    consultar = """
        MATCH (n:Usuario)
        RETURN n
        """
    resultado = graph.run(consultar).data()
    print(resultado)

#listar produto
elif opcao == 6:
    consultar = """
        MATCH (n:Produto)
        RETURN n
        """
    resultado = graph.run(consultar).data()
    print(resultado)

#listar vendedor
elif opcao == 7:
    consultar = """
        MATCH (n:Vendedor)
        RETURN n
        """
    resultado = graph.run(consultar).data()
    print(resultado)

#atualizar dados de usuario
elif opcao == 8:
    nome = input('Digite o nome do usuario: ')
    email = input('Digite o email do usuario: ')
    consultar = """
        MATCH (n:Usuario {nome: $nome})
        SET n.email = $email
        RETURN n
        """
    resultado = graph.run(consultar, nome=nome, email=email).data()
    print(resultado)

#atualizar dados de produto
elif opcao == 9:
    nome = input('Digite o nome do produto: ')
    preco = input('Digite o preco do produto: ')
    consultar = """
        MATCH (n:Produto {nome: $nome})
        SET n.preco = $preco
        RETURN n
        """
    resultado = graph.run(consultar, nome=nome, preco=preco).data()
    print(resultado)

#atualizar dados do vendedor
elif opcao == 10:
    nome = input('Digite o nome do vendedor: ')
    email = input('Digite o email do vendedor: ')
    consultar = """
        MATCH (n:Vendedor {nome: $nome})
        SET n.email = $email
        RETURN n
        """
    resultado = graph.run(consultar, nome=nome, email=email).data()
    print(resultado)

#excluir usuario
elif opcao == 11:
    nome = input('Digite o nome do usuario: ')
    consultar = """
        MATCH (n:Usuario {nome: $nome})
        DETACH DELETE n
        """
    resultado = graph.run(consultar, nome=nome).data()
    print(resultado)

#excluir produto
elif opcao == 12:
    nome = input('Digite o nome do produto: ')
    consultar = """
        MATCH (n:Produto {nome: $nome})
        DETACH DELETE n
        """
    resultado = graph.run(consultar, nome=nome).data()
    print(resultado)

#excluir vendedor
elif opcao == 13:
    nome = input('Digite o nome do vendedor: ')
    consultar = """
        MATCH (n:Vendedor {nome: $nome})
        DETACH DELETE n
        """
    resultado = graph.run(consultar, nome=nome).data()
    print(resultado)

#excluir favorito
elif opcao == 14:
    nome = input('Digite o nome do favorito: ')
    consultar = """
        MATCH (n:Favorito {nome: $nome})
        DETACH DELETE n
        """
    resultado = graph.run(consultar, nome=nome).data()
    print(resultado)

elif opcao == 15:
    #excluir relacao
    nomeUsuario = input('Digite o nome do usuario: ')
    nomeProduto = input('Digite o nome do produto: ')
    consultar = """
        MATCH (a:Usuario {nome: $nomeUsuario})-[r:FAVORITO]->(b:Produto {nome: $nomeProduto})
        DELETE r
        """
    resultado = graph.run(consultar, nomeUsuario=nomeUsuario, nomeProduto=nomeProduto).data()
    print(resultado)
    
else:

    print ( ' \n Opcao invalida! ' )



    


