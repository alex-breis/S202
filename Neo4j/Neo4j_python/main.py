from helper.write_a_json import write_a_json
from db.database import Graph


db = Graph("bolt://44.198.165.206:7687", "neo4j", "jar-discrimination-reaction")

# data = db.execute_query("match (n) return n")
# write_a_json(data, "all_data")


# data = db.execute_query("create (n:Person {name: 'John'}) return n")
# write_a_json(data, "all_data")

def create_person(name):
    data = db.execute_query("create {n:Person {name: $name}} return n" , {'name': name})
    return data

def create_universitario (nome, telefone, idade):
    data = db.execute_query("create (u:Universitario{nome: $nome, telefone: $telefone, idade: $idade})",
    {'nome': nome, 'telefone': telefone, 'idade': idade})
    return data

def create_prof (nome, idade, area):
    data = db.execute_query("create (u:Professor{nome: $nome, idade: $idade, area: $area})",
    {'nome': nome,'idade': idade, 'area': area})
    return data

def create_materia (assunto, horario):
    data = db.execute_query("create (u:Materia{assunto: $assunto, horario: $horario})",
    {'assunto': assunto,'horario': horario})
    return data

def create_leciona (professor, materia, ano):
    data = db.execute_query("MATCH(p:Professor{nome: $nome}),(m:Materia{assunto: $assunto}) CREATE(p)-[:LECIONA{desde: $desde}]->(m);",
    {'nome': professor, 'assunto': materia,'desde': ano})
    return data


create_prof("RenZo", 35, "Computação")
create_prof("Marcelo", 30, "Software")
create_prof("Renan", 40, "Exatas")
create_prof("Dani", 40, "Exatas")

create_materia("Calculo 1", 10)
create_materia("Banco de dados", 21)

create_leciona("Dani","Calculo 1",2015)
create_leciona("RenZo","Banco de dados",2017)
create_leciona("Renan","Calculo 1",2008)