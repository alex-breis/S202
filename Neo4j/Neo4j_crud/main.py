from pprintpp import pprint as pp
from db.database import Graph


class PersonDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.202.30.99:7687',
                        user='neo4j', password='statement-cloths-flight')

    def create(self, person):
        return self.db.execute_query('CREATE (n:Person {name:$name, age:$age}) return n',
                                     {'name': person['name'], 'age': person['age']})

    def read_by_name(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) RETURN n',
                                     {'name': person['name']})
    
    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def update_age(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) SET n.age = $age RETURN n',
                                     {'name': person['name'], 'age': person['age']})

    def delete(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) DELETE n',
                                     {'name': person['name']})

    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')

    def create_relation(self, person1, person2, year):
        return self.db.execute_query('MATCH (n:Person {name:$name1}), (m:Person {name:$name2}) CREATE (n)-[r:KNOWS{year: $year}]->(m) RETURN n, r, m',
                                     {'name1': person1['name'], 'name2': person2['name'], 'year': year})

    def read_relation(self, person1, person2):
        return self.db.execute_query('MATCH (n:Person {name:$name1})-[r]->(m:Person {name:$name2}) RETURN n, r, m',
                                     {'name1': person1['name'], 'name2': person2['name']})

def divider():
    print('\n' + '-' * 80 + '\n')



class CarroDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://3.227.22.102:7687',
                        user='neo4j', password='flowers-second-son')

    def create(self, carro):
        return self.db.execute_query('CREATE (n:Carro {modelo:$modelo, ano:$ano}) return n',
                                     {'modelo': carro['modelo'], 'ano': carro['ano']})

    def read_by_modelo(self, carro):
        return self.db.execute_query('MATCH (n:Carro {modelo:$modelo}) RETURN n',
                                     {'modelo': carro['modelo']})
    
    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def update_ano(self, carro):
        return self.db.execute_query('MATCH (n:Carro {modelo:$modelo}) SET n.ano = $ano RETURN n',
                                     {'modelo': carro['modelo'], 'ano': carro['ano']})

    def delete(self, carro):
        return self.db.execute_query('MATCH (n:Carro {modelo:$modelo}) DELETE n',
                                     {'modelo': carro['modelo']})

    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')

    def create_relation(self, carro1, carro2, marca):
        return self.db.execute_query('MATCH (a:Carro {modelo:$modelo1}), (b:Carro {modelo:$modelo2}) CREATE (a)-[r:MESMA_MARCA {marca: $marca}]->(b) RETURN a, r, b',
                                     {'modelo1': carro1['modelo'], 'modelo2': carro2['modelo'], 'marca': marca})

    def read_relation(self, carro1, carro2):
        return self.db.execute_query('MATCH (a:Carro {modelo:$modelo1})-[r]->(b:Carro {modelo:$modelo2}) RETURN a, r, b',
                                     {'modelo1': carro1['modelo'], 'modelo2': carro2['modelo']})

    def delete_relation(self, carro1, carro2):
        return self.db.execute_query('MATCH (a:Carro {modelo:$modelo1})-[r]->(b:Carro {modelo:$modelo2}) DELETE r',
                                     {'modelo1': carro1['modelo'], 'modelo2': carro2['modelo']})

    def update_relation(self, carro1, carro2, marca):
        return self.db.execute_query('MATCH (a:Carro {modelo:$modelo1})-[r:MESMA_MARCA]->(b:Carro {modelo:$modelo2}) SET r.marca = $marca RETURN a, r, b',
                                     {'modelo1': carro1['modelo'], 'modelo2': carro2['modelo'], 'marca': marca})

dao = CarroDAO()

while 1:    
    option = input('1. Create\n2. Read\n3. Update\n4. Delete\n5. Relação\n')

    if option == '1':
        modelo = input('  Modelo: ')
        ano = input('   Ano: ')
        carro = {
            'modelo': modelo,
            'ano': ano
        }
        aux = dao.create(carro)
        divider()

    elif option == '2':
        aux = dao.read_all_nodes()
        pp(aux)
        divider()

    elif option == '3':
        modelo = input('  Modelo: ')
        ano = input('   Ano: ')
        carro = {
            'modelo': modelo,
            'ano': ano
        }
        
        aux = dao.update_ano(carro)
        divider()

    elif option == '4':
        modelo = input('  Modelo: ')
        carro = {
            'modelo': modelo
        }
        
        aux = dao.delete(carro)
        divider()

    elif option == '5':
        modelo1 = input('  Modelo: ')
        carro1 = {
            'modelo': modelo1,
        }
        modelo2 = input('  Modelo: ')
        carro2 = {
            'modelo': modelo2,
        }
        marca = input('  Marca: ')
        aux = dao.update_relation(carro1,carro2,marca)
        divider()

    else:
        break

# while 1:    
#     option = input('1. Create\n2. Read\n3. Update\n4. Delete\n')

#     if option == '1':
#         name = input('  Name: ')
#         age = input('   Age: ')
#         person = {
#             'name': name,
#             'age': age
#         }
#         aux = dao.create(person)
#         divider()

#     elif option == '2':
#         aux = dao.read_all_nodes()
#         pp(aux)
#         divider()

#     elif option == '3':
#         name = input('  Name: ')
#         age = input('   Age: ')
#         person = {
#             'name': name,
#             'age': age
#         }
        
#         aux = dao.update_age(person)
#         divider()

#     elif option == '4':
#         name = input('  Name: ')
#         person = {
#             'name': name
#         }
        
#         aux = dao.delete(person)
#         divider()

#     else:
#         break

dao.db.close()