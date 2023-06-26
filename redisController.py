import redis
import pymongo
import json
import time
from pymongo.server_api import ServerApi

# Conexão com o Redis
r = redis.Redis(
    host='redis-10412.c262.us-east-1-3.ec2.cloud.redislabs.com',
    port=10412,
    password='ian1902'
)

# Conexão com o MongoDB
client = pymongo.MongoClient("mongodb+srv://iznthelindo:190204@mercadoLivre.1cjw9r7.mongodb.net/mercadoLivre?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.mercadoLivre
collection = db["usuario"]

# Função para inserir um novo usuário no Redis
def iniciarRedis():
    nome = input("Digite o nome: ")

    # Buscar o cliente no MongoDB
    client_data = collection.find_one({"nome": nome})

    if client_data:
        client_json = json.dumps(client_data, default=str)

        # Armazenar o cliente no Redis
        r.set('usuario', client_json)
        print("Cliente inserido no REDIS com sucesso")

        # Obter os dados do Redis
        redis_data = r.get('usuario')

        if redis_data:
            redis_dict = json.loads(redis_data)

            print("\nCadastrar novo favorito")

            new_fav_obj = {
                "id": str(input("Digite um id: ")),
                "favName": str(input("Digite um nome: ")),
                "preco": str(input("Digite um preço: "))
            }

            # Adicionar o novo favorito ao dicionário
            redis_dict.setdefault("favoritos", []).append(new_fav_obj)

            # Converter o dicionário de volta para JSON
            updated_json = json.dumps(redis_dict, default=str)

            # Atualizar os dados no Redis
            r.set('usuario', updated_json)

            # Atualizar os dados no MongoDB
            collection.update_one({"_id": client_data["_id"]}, {"$set": {"favoritos": redis_dict["favoritos"]}})

            print("Novo favorito cadastrado")

            Fast_Buy = input("Digite o seu Fast Buy: ")
            collection.update_one({"_id": client_data["_id"]}, {"$set": {"Fast_Buy": Fast_Buy}})
            print("Fast Buy adicionado! Você tem 10s para comprar tudo pela metade do preço")

            time.sleep(10)

            collection.update_one({"_id": client_data["_id"]}, {"$unset": {"Fast_Buy": ""}})
            print("Fast Buy removido!")


            # Timer de 10 segundos
            print("Aguardando 10 segundos...")
            time.sleep(10)
            print("Timer de 10 segundos expirado.")

        else:
            print("Erro ao obter os dados do Redis")
    else:
        print("Cliente não encontrado no MongoDB")



# Chamar a função iniciarRedis para executar o código
iniciarRedis()
