from db.database import Database
from helper.WriteAJson import writeAJson

db = Database()

# tipos = ["Grass", "Poison"]
pokemons = db.executeQuery({"weaknesses": "Ground" })

writeAJson(data=pokemons, name="Pokemons")
