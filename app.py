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

print("--- BEM VINDO AO MERCADO LIVRE ---")

def insert(nome, cpf, email, rua, numero, bairro, cidade, estado, cep):
    global mydb
    mycol = mydb.usuario
    print("\n####INSERT####")
    mydict = {"nome": nome, "cpf": cpf, "email": email, "rua": rua, "numero": numero, "bairro": bairro, "cidade": cidade, "estado": estado, "cep": cep}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insertproduto(produto, quantidade, preco):
    global mydb
    mycolprod = mydb.produtos
    print("\n####INSERT####")
    mydict = {"produto": produto, "quantidade": quantidade, "preco": preco}
    x = mycolprod.insert_one(mydict)
    print(x.inserted_id)

def insertvendedor(vendedor, codigo):
    global mydb
    mycolvend = mydb.vendedor
    print("\n####INSERT####")
    mydict = {"vendedor": vendedor, "codigo": codigo}
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

def delete(query):
    global mydb
    mycol = mydb.usuario
    print("\n####DELETE####")
    x = mycol.delete_many(query)
    print(x.deleted_count, " documento(s) deletado(s).")

def deletevendedor(query):
    global mydb
    mycolvend = mydb.vendedor
    print("\n####DELETE####")
    x = mycolvend.delete_many(query)
    print(x.deleted_count, " documento(s) deletado(s).")

def deletecompras(query):
    global mydb
    mycolcom = mydb.compras
    print("\n####DELETE####")
    x = mycolcom.delete_many(query)
    print(x.deleted_count, " documento(s) deletado(s).")

def deletefavoritos(query):
    global mydb
    mycolfav = mydb.favoritos
    print("\n####DELETE####")
    x = mycolfav.delete_many(query)
    print(x.deleted_count, " documento(s) deletado(s).")


def deleteprodutos(query):
    global mydb
    mycolprod = mydb.produtos
    print("\n####DELETE####")
    x = mycolprod.delete_many(query)
    print(x.deleted_count, " documento(s) deletado(s).")

def update(query, newvalues):
    global mydb
    mycol = mydb.usuario
    print("\n####UPDATE####")
    x = mycol.update_many(query, newvalues)
    print(x.modified_count, " documento(s) atualizado(s).")

def updatevendedor(query, newvalues):
    global mydb
    mycolvend = mydb.vendedor
    print("\n####UPDATE####")
    x = mycolvend.update_many(query, newvalues)
    print(x.modified_count, " documento(s) atualizado(s).")

def updatecompras(query, newvalues):
    global mydb
    mycolcom = mydb.compras
    print("\n####UPDATE####")
    x = mycolcom.update_many(query, newvalues)
    print(x.modified_count, " documento(s) atualizado(s).")

def updatefavoritos(query, newvalues):
    global mydb
    mycolfav = mydb.favoritos
    print("\n####UPDATE####")
    x = mycolfav.update_many(query, newvalues)
    print(x.modified_count, " documento(s) atualizado(s).")

def updateprodutos(query, newvalues):
    global mydb
    mycolprod = mydb.produtos
    print("\n####UPDATE####")
    x = mycolprod.update_many(query, newvalues)
    print(x.modified_count, " documento(s) atualizado(s).")

def main():
    while True:
        print("\n----- MENU -----")
        print("1 - Inserir usuário")
        print("2 - Inserir produto")
        print("3 - Inserir vendedor")
        print("4 - Inserir compra")
        print("5 - Inserir favorito")
        print("6 - Ordenar usuários por nome")
        print("7 - Ordenar produtos por nome")
        print("8 - Ordenar vendedores por nome")
        print("9 - Ordenar compras por valor")
        print("10 - Ordenar favoritos por nome")
        print("11 - Deletar usuário")
        print("12 - Deletar vendedor")
        print("13 - Deletar compra")
        print("14 - Deletar favorito")
        print("15 - deletar produto")
        print("16 - Atualizar usuário")
        print("17 - Atualizar vendedor")
        print("18 - Atualizar compra")
        print("19 - Atualizar favorito")
        print("20 - Atualizar produto")
        print("0 - Sair")

        choice = int(input("Escolha uma opção: "))

        if choice == 1:
            nome = input("Digite o nome do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            email = input("Digite o e-mail do usuário: ")
            rua = input("Digite o nome da rua: ")
            numero = input("Digite o número da rua: ")
            bairro = input("Digite o nome do bairro: ")
            cidade = input("Digite o nome da cidade: ")
            estado = input("Digite o nome do estado: ")
            cep = input("Digite o CEP: ")
            insert(nome, cpf, email, rua, numero, bairro, cidade, estado, cep)

        elif choice == 2:
            produto = input("Digite o nome do produto: ")
            quantidade = input("Digite a quantidade do produto: ")
            preco = input("Digite o preço do produto: ")
            insertproduto(produto, quantidade, preco)

        elif choice == 3:
            vendedor = input("Digite o nome do vendedor: ")
            codigo = input("Digite o código do vendedor: ")
            insertvendedor(vendedor, codigo)

        elif choice == 4:
            nome_prod = input("Digite o nome do produto: ")
            codigo = input("Digite o código da compra: ")
            valor = input("Digite o valor da compra: ")
            insertcompras(nome_prod, codigo, valor)

        elif choice == 5:
            nome_prod = input("Digite o nome do produto: ")
            codigo = input("Digite o código do favorito: ")
            insertfavoritos(nome_prod, codigo)

        elif choice == 6:
            findSort("nome")

        elif choice == 7:
            findSortprodutos("produto")

        elif choice == 8:
            findSortvendedor("vendedor")

        elif choice == 9:
            findSortcompras("valor")

        elif choice == 10:
            findSortfavoritos("nomeprod")

        elif choice == 11:
            cpf = input("Digite o CPF do usuário a ser deletado: ")
            query = {"cpf": cpf}
            delete(query)

        elif choice == 12:
            codigo = input("Digite o código do vendedor a ser deletado: ")
            query = {"codigo": codigo}
            deletevendedor(query)

        elif choice == 13:
            codigo = input("Digite o código da compra a ser deletada: ")
            query = {"codigo": codigo}
            deletecompras(query)

        elif choice == 14:
            codigo = input("Digite o código do favorito a ser deletado: ")
            query = {"codigo": codigo}
            deletefavoritos(query)

        elif choice == 15:
            produto = input("Digite o nome do produto a ser deletado: ")
            query = {"produto": produto}
            deleteprodutos(query)

        elif choice == 16:
            cpf = input("Digite o CPF do usuário a ser atualizado: ")
            query = {"cpf": cpf}
            nome = input("Digite o novo nome do usuário: ")
            newvalues = {"$set": {"nome": nome}}
            update(query, newvalues)

        elif choice == 17:
            codigo = input("Digite o código do vendedor a ser atualizado: ")
            query = {"codigo": codigo}
            vendedor = input("Digite o novo nome do vendedor: ")
            newvalues = {"$set": {"vendedor": vendedor}}
            updatevendedor(query, newvalues)

        elif choice == 18:
            codigo = input("Digite o código da compra a ser atualizada: ")
            query = {"codigo": codigo}
            valor = input("Digite o novo valor da compra: ")
            newvalues = {"$set": {"valor": valor}}
            updatecompras(query, newvalues)

        elif choice == 19:
            codigo = input("Digite o código do favorito a ser atualizado: ")
            query = {"codigo": codigo}
            nome_prod = input("Digite o novo nome do produto: ")
            newvalues = {"$set": {"nomeprod": nome_prod}}
            updatefavoritos(query, newvalues)

        elif choice == 20:
            produto = input("Digite o nome do produto a ser atualizado: ")
            query = {"produto": produto}
            quantidade = input("Digite a nova quantidade do produto: ")
            newvalues = {"$set": {"quantidade": quantidade}}
            updateprodutos(query, newvalues)    

        elif choice == 0:
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()




