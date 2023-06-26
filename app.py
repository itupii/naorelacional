import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://iznthelindo:190204@mercadoLivre.1cjw9r7.mongodb.net/mercadoLivre?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.mercadoLivre

global mydb
mydb = client.mercadoLivre

mycol = ["usuario"]
mycolvend = ["vendedor"]
mycolprod = ["produtos"]
mycolfav = ["favoritos"]
mycolcom = ["compras"]


def insert(nome, cpf, email, rua, numero, bairro, cidade, estado, cep, favorito, preço):
    global mydb
    mycol = mydb.usuario
    print("\n####INSERT####")
    mydict = {"nome": nome, "cpf": cpf, "email": email, "rua": rua, "numero": numero, "bairro": bairro, "cidade": cidade, "estado": estado, "cep": cep, "favorito": favorito, "preço": preço}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insertproduto(produto, quantidade, preco):
    global mydb
    mycolprod = mydb.produtos
    print("\n####INSERT####")
    mydict = {"produto": produto, "quantidade": quantidade, "preco": preco}
    x = mycolprod.insert_one(mydict)
    print(x.inserted_id)

def insertvendedor(vendedor, codigo, produtoVendido):
    global mydb
    mycolvend = mydb.vendedor
    print("\n####INSERT####")
    mydict = {"vendedor": vendedor, "codigo": codigo, "produtoVendido": produtoVendido}
    x = mycolvend.insert_one(mydict)
    print(x.inserted_id)

def insertcompras(nome_prod, codigo, valor):
    global mydb
    mycolcom = mydb.compras
    print("\n####INSERT####")
    mydict = {"nomeprod": nome_prod, "codigo": codigo, "valor": valor}
    x = mycolcom.insert_one(mydict)
    print(x.inserted_id)

def insertfavoritos(nome_prod, codigo):
    global mydb
    mycolfav = mydb.favoritos
    print("\n####INSERT####")
    mydict = {"nomeprod": nome_prod, "codigo": codigo}
    x = mycolfav.insert_one(mydict)
    print(x.inserted_id)

def findSort(nome):
    global mydb
    mycol = mydb.usuario
    print("\n####SORT####")
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)

def findSortprodutos(produto):
    global mydb
    mycolprod = mydb.produtos
    print("\n####SORT####")
    mydoc = mycolprod.find().sort(produto)
    for x in mydoc:
        print(x)

def findSortvendedor(vendedor):
    global mydb
    mycolvend = mydb.vendedor
    print("\n####SORT####")
    mydoc = mycolvend.find().sort(vendedor)
    for x in mydoc:
        print(x)

def findSortcompras(compras):
    global mydb
    mycolcom = mydb.compras
    print("\n####SORT####")
    mydoc = mycolcom.find().sort(compras)
    for x in mydoc:
        print(x)

def findSortfavoritos(favoritos):
    global mydb
    mycolfav = mydb.favoritos
    print("\n####SORT####")
    mydoc = mycolfav.find().sort(favoritos)
    for x in mydoc:
        print(x)

def find(nome):
    global mydb
    mycol = mydb.usuario
    print("\n####FIND####")
    myquery = {"nome": nome}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def findprodutos(produto):
    global mydb
    mycolprod = mydb.produtos
    print("\n####FIND####")
    myquery = {"produto": produto}
    mydoc = mycolprod.find(myquery)
    for x in mydoc:
        print(x)

def findvendedor(vendedor):
    global mydb
    mycolvend = mydb.vendedor
    print("\n####FIND####")
    myquery = {"vendedor": vendedor}
    mydoc = mycolvend.find(myquery)
    for x in mydoc:
        print(x)

def findcompras(compras):
    global mydb
    mycolcom = mydb.compras
    print("\n####FIND####")
    myquery = {"compras": compras}
    mydoc = mycolcom.find(myquery)
    for x in mydoc:
        print(x)

def findfavoritos(favoritos):
    global mydb
    mycolfav = mydb.favoritos
    print("\n####FIND####")
    myquery = {"favoritos": favoritos}
    mydoc = mycolfav.find(myquery)
    for x in mydoc:
        print(x)

def deleteOne(nome):
    global mydb
    mycol = mydb.usuario
    print("\n####DELETE####")
    myquery = {"nome": nome}
    mycol.delete_one(myquery)
    print("Registro deletado com sucesso!")

def deleteOneprod(produto):
    global mydb
    mycolprod = mydb.produtos
    print("\n####DELETE####")
    myquery = {"produto": produto}
    mycolprod.delete_one(myquery)
    print("Registro deletado com sucesso!")

def deleteOnevendedor(vendedor):
    global mydb
    mycolvend = mydb.vendedor
    print("\n####DELETE####")
    myquery = {"vendedor": vendedor}
    mycolvend.delete_one(myquery)
    print("Registro deletado com sucesso!")

def deleteOnecompras(compras):
    global mydb
    mycolcom = mydb.compras
    print("\n####DELETE####")
    myquery = {"compras": compras}
    mycolcom.delete_one(myquery)
    print("Registro deletado com sucesso!")

def deleteOnefavoritos(favoritos):
    global mydb
    mycolfav = mydb.favoritos
    print("\n####DELETE####")
    myquery = {"favoritos": favoritos}
    mycolfav.delete_one(myquery)
    print("Registro deletado com sucesso!")


while True:
    print("\n========================")
    print("     MERCADO LIVRE")
    print("========================")
    print("1 - Inserir usuário")
    print("2 - Inserir produto")
    print("3 - Inserir vendedor")
    print("4 - Inserir compras")
    print("5 - Inserir favoritos")
    print("6 - Ordenar usuários por nome")
    print("7 - Ordenar produtos por nome")
    print("8 - Ordenar vendedores por nome")
    print("9 - Ordenar compras por nome")
    print("10 - Ordenar favoritos por nome")
    print("11 - Buscar usuário")
    print("12 - Buscar produto")
    print("13 - Buscar vendedor")
    print("14 - Buscar compras")
    print("15 - Buscar favoritos")
    print("16 - Deletar usuário")
    print("17 - Deletar produto")
    print("18 - Deletar vendedor")
    print("19 - Deletar compras")
    print("20 - Deletar favoritos")
    print("0 - Sair")
    op = int(input("Digite uma opção: "))

    if op == 1:
        nome = input("Digite o nome do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        email = input("Digite o email do usuário: ")
        rua = input("Digite a rua do usuário: ")
        numero = input("Digite o número da casa do usuário: ")
        bairro = input("Digite o bairro do usuário: ")
        cidade = input("Digite a cidade do usuário: ")
        estado = input("Digite o estado do usuário: ")
        cep = input("Digite o CEP do usuário: ")
        favorito = input("Digite o favorito do usuário: ")
        preço = input("Digite o preço do produto: ")
        insert(nome, cpf, email, rua, numero, bairro, cidade, estado, cep, favorito, preço)
    elif op == 2:
        produto = input("Digite o nome do produto: ")
        quantidade = input("Digite a quantidade do produto: ")
        preco = input("Digite o preço do produto: ")
        insertproduto(produto, quantidade, preco)
    elif op == 3:
        vendedor = input("Digite o nome do vendedor: ")
        codigo = input("Digite o código do vendedor: ")
        produtoVendido = input("Digite o produto vendido pelo vendedor: ")
        insertvendedor(vendedor, codigo, produtoVendido)
    elif op == 4:
        nome_prod = input("Digite o nome do produto: ")
        codigo = input("Digite o código do produto: ")
        valor = input("Digite o valor do produto: ")
        insertcompras(nome_prod, codigo, valor)
    elif op == 5:
        nome_prod = input("Digite o nome do produto: ")
        codigo = input("Digite o código do produto: ")
        insertfavoritos(nome_prod, codigo)
    elif op == 6:
        findSort("nome")
    elif op == 7:
        findSortprodutos("produto")
    elif op == 8:
        findSortvendedor("vendedor")
    elif op == 9:
        findSortcompras("compras")
    elif op == 10:
        findSortfavoritos("favoritos")
    elif op == 11:
        nome = input("Digite o nome do usuário: ")
        find(nome)
    elif op == 12:
        produto = input("Digite o nome do produto: ")
        findprodutos(produto)
    elif op == 13:
        vendedor = input("Digite o nome do vendedor: ")
        findvendedor(vendedor)
    elif op == 14:
        compras = input("Digite a compra: ")
        findcompras(compras)
    elif op == 15:
        favoritos = input("Digite o favorito: ")
        findfavoritos(favoritos)
    elif op == 16:
        nome = input("Digite o nome do usuário que deseja deletar: ")
        deleteOne(nome)
    elif op == 17:
        produto = input("Digite o nome do produto que deseja deletar: ")
        deleteOneprod(produto)
    elif op == 18:
        vendedor = input("Digite o nome do vendedor que deseja deletar: ")
        deleteOnevendedor(vendedor)
    elif op == 19:
        compras = input("Digite a compra que deseja deletar: ")
        deleteOnecompras(compras)
    elif op == 20:
        favoritos = input("Digite o favorito que deseja deletar: ")
        deleteOnefavoritos(favoritos)
    elif op == 0:
        break
    else:
        print("Opção inválida. Digite novamente.")
