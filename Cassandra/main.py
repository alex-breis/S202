from db.database import Database
from cassandra.protocol import ProtocolException

db = Database(client_id='vDKlBjJoIsrkosITeRSbjQAS',
    client_secret='.h5UUFUHCt6UDrEeumg_zLKILwNk.,Y6E49cCgFQEIyFCMelFigTsbuygt-86XJ.2K9lZu.WX7pucYWBrQ4Jw8WZx_ocEy1,b1Js7c3gs,tI4fAGkW7MgaRqvGA0.SwL',
    keyspace='estoque')
    
'''
Questão 01 
'''
# a.
def create_estoque(self, id, nome, carro, estante, nivel, quantidade):
    try:
        query= "INSERT INTO estoque (id, nome, carro, estante, nivel, quantidade)"\
        f"VALUES({id},'{nome}','{carro}',{estante},{nivel},{quantidade})"
        self.session.execute(query)
    except ProtocolException as ex:
            print(f'Erro ao inserir estoque: {ex}')

# b 
db.create_estoque(5, "Pistão", "Mustang", 4, 1, 167)
db.create_estoque(4, "Suspencao", "Argo", 1, 1, 3500)


'''
Para a questão 2 não é necessario utilizar o python, apenas insira as query's neste comentario.

Questão 02:
a. CREATE INDEX userIndex ON estoque(estante);
b. SELECT nome,carro,quantidade FROM estoque WHERE estante = 3;
c. CREATE INDEX userIndex1 ON estoque(nivel);
d. SELECT AVG(quantidade) FROM estoque WHERE nivel = 1;
e. SELECT * FROM estoque WHERE estante < 3 AND nivel > 4;

'''
