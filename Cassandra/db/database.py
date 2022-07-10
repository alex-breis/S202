from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.protocol import ProtocolException

class Database(object):
    def __init__(self, client_id,client_secret,keyspace):
        cloud_config = {
            'secure_connect_bundle': './secure-connect-database.zip'
        }
        auth_provider = PlainTextAuthProvider(client_id, client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()
        self.session.set_keyspace(keyspace)
    def create_estoque(self, id, nome, carro, estante, nivel, quantidade, tempo):
        try:
            query= "INSERT INTO estoque (id, nome, carro, estante, nivel, quantidade)"\
            f"VALUES({id},'{nome}','{carro}',{estante},{nivel},{quantidade})"
            self.session.execute(query)
        except ProtocolException as ex:
                print(f'Erro ao inserir estoque: {ex}')