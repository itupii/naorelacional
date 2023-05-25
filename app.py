import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId





client = pymongo.MongoClient("mongodb+srv://iznthelindo:190204@mercadoLivre.1cjw9r7.mongodb.net/mercadoLivre?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.mercadoLivre

global mydb
mydb = client.mercadoLivre

mycol     = ["usuario"]
mycolvend = ["vendedor"]
mycolprod = ["produtos"]
mycolfav =  ["favoritos"]
mycolcom =  ["compras"]


print ("--- BEM VINDO AO MERCADO LIVRE ---")

print ("\n cadastro ")

print ("1 - cadastrar usuario")
print ("2 - cadastro de produto ")
print ("3 - cadastro de vendedor ")
print ("4 - cadastro de compras ")
print ("5 - cadastro de favoritos ")


print ("\n CONSULTA GERAL ")

print ("6 - consulta geral de usuario")
print ("7 - consulta geral de produto")
print ("8 - consulta geral de vendedor")
print ("9- consulta geral de compras")
print ("10- consulta geral de favoritos")


print ("\n cCONSULTA ESPECIFICA ")
print ("11- consultar usuario")
print ("11.1- listar usuario")
print ("12 - consultar produto")
print ("13 - consultar vendedor")
print ("14 - consultar compras")
print ("15 - consultar favoritos")


print ("\n ATUALIZAR *** ")

print ("16 - atualizar usuario")
print ("17 - atualizar produto")
print ("18 - atualizar vendedor")
print ("19 - atualizar compras")
print ("20 - atualizar favoritos")


print ("\n DELETAR ***")
print ("21 - deletar usuario")
print ("22 - deletar produto")
print ("23 - deletar vendedor")
print ("24 - deletar compras")
print ("25 - deletar favoritos")

print ("SAIR")
opção = int(input("Digite a opção desejada: "))


def insert(nome, cpf,email, rua, numero, bairro, cidade, estado, cep):
    #Insert
    global mydb
    mycol = mydb.usuario
    print("\n####INSERT####")
    mydict = { "nome": nome, "cpf":cpf, "email":email,  "rua": rua, "numero": numero, "bairro": bairro, "cidade": cidade, "estado": estado, "cep": cep}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

if opção == 1:
    nome = str(input("digite seu nome: "))
    cpf = str(input("digite seu cpf: "))
    email =  str(input("digite seu email: "))
    rua =    str(input("digite sua rua: "))
    numero = str(input("digite seu numero: "))
    bairro = str(input("digite seu bairro: "))
    cidade = str(input("digite sua cidade: "))
    estado = str(input("digite seu estado: "))
    cep =    str(input("digite seu cep: "))

    insert(nome, cpf, email, rua, numero,bairro , cidade, estado, cep)

def insertproduto(produto ,quantidade , preco):
    
    global mydb
    mycolprod = mydb.produtos
    print("\n####INSERT####")
    mydict = { "produto": produto, "quantidade":quantidade, "preco":preco }
    x = mycolprod.insert_one(mydict)
    print(x.inserted_id)

if opção == 2:
    produto = str(input("produto: "))
    quantidade = str(input("digite a quantidade: "))
    preco = str(input("digite o preço final: "))

    insertproduto(produto, quantidade, preco)



def insertvendedor(vendedor, codigo):
    
    global mydb
    mycolvend = mydb.vendedor
    print("\n####INSERT####")
    mydict = { "vendedor": vendedor, "codigo": codigo,  }
    x = mycolvend.insert_one(mydict)
    print(x.inserted_id)

if opção == 3:
    vendedor= str(input("nome do vendedor : "))
    código = str(input("digite o código do vendedor: "))
    end = []

    insertvendedor(vendedor, código)


def insertcompras(nome_prod, codigo, valor):

    global mydb
    mycolcom = mydb.compras
    print("\n####INSERT####")
    mydict = { "nomeprod": nome_prod, "codigo": codigo, "valor": valor  }
    x = mycolcom.insert_one(mydict)
    print(x.inserted_id)

if opção == 4:
    nome_prod = str(input("nome do produto: "))
    código = int(input("digite o código do produto: "))
    valor =  str(input("digite o valor do produto: "))
    end = []

    insertcompras(nome_prod, código, valor)

def insertfavoritos(nome_prod, codigo):

    global mydb
    mycolfav = mydb.favoritos
    print("\n####INSERT####")
    mydict = { "nomeprod": nome_prod, "codigo": codigo,  }
    x = mycolfav.insert_one(mydict)
    print(x.inserted_id)

if opção == 5:
    nome_prod = str(input("nome do produto: "))
    código = str(input("digite o código do produto: "))
    end = []

    insertfavoritos(nome_prod, código)




def findSort(nome):
    #Sort
    global mydb
    mycol = mydb.usuario
    print("\n####SORT####") 
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)

if opção == 6:
    findSort("nome")

def findSortprodutos(produto):
    
    global mydb
    mycolprod = mydb.produtos
    print("\n####SORT####") 
    mydoc = mycolprod.find().sort(produto)
    for x in mydoc:
        print(x)

if opção == 7:
    findSortprodutos("produto")

def findSortvendedor(vendedor):

    global mydb
    mycolvend = mydb.vendedor
    print("\n####SORT####")
    mydoc = mycolvend.find().sort(vendedor)
    for x in mydoc:
        print(x)

if opção == 8:
    findSortvendedor("vendedor")

def findSortcompras(compras):

    global mydb
    mycolcom = mydb.compras
    print("\n####SORT####")
    mydoc = mycolcom.find().sort(compras)
    for x in mydoc:
        print(x)

if opção == 9:
    findSortcompras("compras")

def findSortfavoritos(favoritos):
    
        global mydb
        mycolfav = mydb.favoritos
        print("\n####SORT####")
        mydoc = mycolfav.find().sort(favoritos)
        for x in mydoc:
            print(x)

if opção == 10:
    findSortfavoritos("favoritos")




def findQuery(nome):
    #Query
    global mydb
    mycol = mydb.usuario
    print("\n####QUERY####")
    myquery = { "nome": nome }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

if opção == 11:
    nome = str(input("digite o nome do usuario: "))
    findQuery(nome)

def findQueryprodutos(produtos):

    global mydb
    mycolprod = mydb.produtos
    print("\n####QUERY####")
    myquery = { "produto": produtos}
    mydoc = mycolprod.find(myquery)
    for x in mydoc:
        print(x)



if opção == 11.1:
    listarusuarios = str(input("digite o nome do usuario: "))
    findQuery(listarusuarios)

def findQueryUsuarios (nome):

    global mydb
    mycol = mydb.usuario
    print("\n####QUERY####")
    myquery = { "nome": nome }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

if opção == 12:
   produtos = str(input("digite o nome do produto: "))
   findQueryprodutos(produtos)

def findQueryvendedor(vendedor):

    global mydb
    mycolvend = mydb.vendedor
    print("\n####QUERY####")
    myquery = { "vendedor": vendedor}
    mydoc = mycolvend.find(myquery)
    for x in mydoc:
        print(x)

if opção == 13:
    vendedor = str(input("digite o nome do vendedor: "))
    findQueryvendedor(vendedor)

def findQuerycompras(compras):

    global mydb
    mycolcom = mydb.compras
    print("\n####QUERY####")
    myquery = { "compras": compras }
    mydoc = mycolcom.find(myquery)
    for x in mydoc:
        print(x)

if opção == 14:
    compras = str(input("digite o nome da compra: "))
    findQuerycompras(compras)

def findQueryfavoritos(favoritos):

    global mydb
    mycolfav = mydb.favoritos
    print("\n####QUERY####")
    myquery = { "favoritos": favoritos }
    mydoc = mycolfav.find(myquery)
    for x in mydoc:
        print(x)

if opção == 15:
    favoritos = str(input("digite o nome do favorito: "))
    findQueryfavoritos(favoritos)


def updateQuery(nome, cpf, email, rua, numero, bairro, cidade, estado, cep):

    global mydb
    mycol = mydb.usuario
    print("\n####UPDATE####")
    myquery = { "nome": nome }
    newvalues = { "$set": { "nome": nome , "cpf": cpf, "email": email, "rua":rua, "numero":numero, "bairro":bairro,"cidade":cidade, "estado": estado, "cep": cep  } }
    mycol.update_one(myquery, newvalues)
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

if opção == 16:
    nome = str(input("digite o  novo nome do usuario: "))
    cpf = int(input("digite o  novo cpf do usuario: "))
    email = str(input("digite o  novo email do usuario: "))
    rua = str(input("digite a  nova rua do usuario: "))
    numero = int(input("digite o  novo numero do usuario: "))
    bairro = str(input("digite o  novo bairro do usuario: "))
    cidade = str(input("digite a  nova cidade do usuario: "))
    estado = str(input("digite o  novo estado do usuario: "))
    cep = int(input("digite o  novo cep do usuario: "))

    updateQuery(nome, cpf, email,rua, numero, bairro, cidade, estado, cep )

def updateQueryprodutos(produto, quantidade,preco):

    global mydb
    mycol = mydb.usuario
    print("\n####UPDATE####")
    myquery = { "produto": produto }
    newvalues = { "$set": { "produto": produto , "quantidade": quantidade, "preco": preco } }
    mycol.update_one(myquery, newvalues)
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)
if opção == 17:

    nome = str(input("digite o nome do produto: "))
    quantidade =int(input("digite a quantidade do produto: "))
    preco = int(input("digite o preço do produto: "))
    updateQueryprodutos( produto, quantidade, preco)

def updateQueryvendedor(vendedor, código):

    global mydb
    mycolvend = mydb.vendedor
    print("\n####UPDATE####")
    myquery = { "vendedor": vendedor, "codigo": código  }
    newvalues = { "$set": {"vendedor": vendedor, "codigo": código } }
  

if opção == 18:
    vendedor = str(input("digite o nome do vendedor: "))
    código = int(input("digite o código do vendedor: "))
    updateQueryvendedor(vendedor, código)

def updateQuerycompras(compras, quantidade, valor):

    global mydb
    mycolcom = mydb.compras
    print("\n####UPDATE####")
    myquery = { "compras": compras, "quantidade": quantidade, "valor": valor }
    newvalues = { "$set": {"compras": compras, "quantidade": quantidade, "valor": valor } }

if opção == 19:
        compras = str(input("digite o nome da compra: "))
        quantidade = int(input("digite a quantidade da compra: "))
        valor = int(input("digite o valor da compra: "))
        updateQuerycompras(compras, quantidade, valor)

def updateQueryfavoritos(favoritos, quantidade, valor):

    global mydb
    mycolfav = mydb.favoritos
    print("\n####UPDATE####")
    myquery = { "favoritos": favoritos, "quantidade": quantidade, "valor": valor }
    newvalues = { "$set": {"favoritos": favoritos, "quantidade": quantidade, "valor": valor } }

if opção == 20:

    favoritos = str(input("digite o nome do favorito: "))
    quantidade = int(input("digite a quantidade do favorito: "))
    valor = int(input("digite o valor do favorito: "))
    updateQueryfavoritos(favoritos, quantidade, valor)




def deleteQuery(cpf):

    global mydb
    mycol = mydb.usuario
    print("\n####DELETE####")
    myquery = { "cpf": cpf }
    mycol.delete_one(myquery)
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

if opção == 21:
    cpf =int(input("digite o cpf do usuario: "))
    deleteQuery(cpf)



def deleteQueryvendedor( codigo):

    global mydb
    mycolvend = mydb.vendedor
    print("\n####DELETE####")
    myquery = {"codigo": codigo}
    mycolvend.delete_one(myquery)
    mydoc = mycolvend.find(myquery)

if opção == 23:
    codigo = str(input("digite o codigo do vendedor:"))
    deleteQueryvendedor(codigo)

    

def deleteQuerycompras(compras):
    global mydb
    mycolcom = mydb.compras
    print("\n####DELETE####")
    print("\nDeletado com sucesso!")
    myquery = { "compras": compras }
    mycolcom.delete_one(myquery)
    mydoc = mycolcom.find(myquery)
    for x in mydoc:
        print(x)

if opção == 24:
    compras = str(input("digite o nome da compra: " ))
    deleteQuerycompras(compras)

def deleteQueryfavoritos(codigo):

    global mydb
    mycolfav = mydb.favoritos
    print("\n####DELETE####")
    print("\nDeletado com sucesso!")
    myquery = { "codigo": codigo}
    mycolfav.delete_one(myquery)
    mydoc = mycolfav.find(myquery)


if opção == 25:
    print(mycolfav)
    codigo = str(input("digite o nome do seu favoritado: "))

    
    deleteQueryfavoritos(codigo)
















