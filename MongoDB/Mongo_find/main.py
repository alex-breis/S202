from gettext import find
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

tipos=["Grass","Poison"]
pokemons = db.collection.find({"type": {"$all": tipos}}) #Pokemons contendo os tipos Grass e Poison

pokemons = db.collection.find({"type": {"$size": 2}}) #Pokemons que possuem dois tipos

pokemons = db.collection.find({"next_evolution": {"$exists": False}, "prev_evolution": {"$exists": False}}) #Pokemons sem evolução

pokemons = db.collection.find({"avg_spawns": {"$lt": 1}})  #Pokemons com média de spawn menor que 1

pokemons = db.collection.find({"egg": { "$eq": "Not in Eggs" }})  #Pokemons não obtidos por Eggs


# pokemons = db.collection.find({"spawm_chance": {"$gt": 1}},
# {
#     "name":1,
#     "spawm_chance": 1,
#     "_id":0
# })

writeAJson(data=pokemons, name="Pokemons")