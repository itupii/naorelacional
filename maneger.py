from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

class MercadoLivreDB:
    def __init__(self, secure_bundle_path, client_id, client_secret):
        cloud_config = {'secure_connect_bundle': secure_bundle_path}
        auth_provider = PlainTextAuthProvider(client_id, client_secret)
        self.cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = self.cluster.connect()

    def create_keyspace(self, keyspace_name):
        query = f"CREATE KEYSPACE IF NOT EXISTS {keyspace_name} WITH REPLICATION = {{ 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 1 }}"
        self.session.execute(query)

    def use_keyspace(self, keyspace_name):
        query = f"USE {keyspace_name}"
        self.session.execute(query)

    def create_table(self, table_name, columns):
        columns_str = ', '.join(columns)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str}, PRIMARY KEY ((id)))"
        self.session.execute(query)

    def insert_data(self, table_name, values):
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['%s'] * len(values))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.session.execute(query, tuple(values.values()))

    def update_data(self, table_name, values, condition):
        set_values = ', '.join([f"{column} = %s" for column in values.keys()])
        query = f"UPDATE {table_name} SET {set_values} WHERE {condition}"
        self.session.execute(query, tuple(values.values()))

    def search_data(self, table_name, condition):
        query = f"SELECT * FROM {table_name} WHERE {condition}"
        result = self.session.execute(query)
        return result

    def delete_data(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.session.execute(query)

    def close_connection(self):
        self.session.shutdown()
        self.cluster.shutdown()

# Exemplo de uso

# Configuração inicial
secure_bundle_path = './secure-connect-mercadolivredb.zip'
client_id = 'BuBEchYmSlumjBjbjeaElsOy'
client_secret = 'Q_jJOR8Dv9Rm7QPwJBc1zp9RfpTLqgKk9eGO0m_f.FcfR,nFmFSjUrBqbr7+L6EZnSoOxO6Qyj_Dg39SQXv-ivfZq4wPvw7Wg0wljsn.ovKtU.O5Zx7zgmDo9KQXw0_0'

# Instanciar o objeto MercadoLivreDB
db = MercadoLivreDB(secure_bundle_path, client_id, client_secret)

# Criar e usar o keyspace
keyspace_name = 'mercadolivre'
db.use_keyspace(keyspace_name)

# Criar tabela 'usuario'
usuario_table_name = 'usuario'
usuario_columns = ['id UUID', 'nome TEXT', 'email TEXT']
db.create_table(usuario_table_name, usuario_columns)

# Inserir dados na tabela 'usuario'
usuario_values = {'id': uuid.uuid4(), 'nome': 'ian', 'email': 'john@example.com'}
db.insert_data(usuario_table_name, usuario_values)

# Restante do código para atualizar, pesquisar e deletar...

# Fechar conexão
db.close_connection()
