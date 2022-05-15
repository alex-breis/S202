from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.pessoa_dataset import dataset as pessoa_dataset
from dataset.carro_dataset import dataset as carro_dataset
from dataset.produto_database import dataset as produto_dataset

pessoas = Database(
    database="database",
    collection="pessoas",
    dataset=pessoa_dataset
)
# pessoas.resetDatabase()

carros = Database(
    database="database",
    collection="carros",
    dataset=carro_dataset
)
# carros.resetDatabase()

# resultado = carros.collection.aggregate([
#     {"$lookup":
#         {
#             "from": "pessoas",  # outra colecao
#             "localField": "dono_id",  # chave estrangeira
#             "foreignField": "_id",  # id da outra colecao
#             "as": "dono"  # nome da saida
#         }
#      }
# ])

produtos = Database(
    database="database",
    collection="produtos",
    dataset=produto_dataset
)
# produtos.resetDatabase()

resultado = produtos.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",
            "localField": "cliente_id",
            "foreignField": "_id",
            "as": "Cliente"
        }
    },
    {
        "$group": {"_id": "$Cliente", "total": {"$sum": "$total"} } 
    },
    {"$sort": {"total": 1} },
    {"$unwind": '$_id'},  #Tira a pessoa do array
    {"$project": {
        "_id": 0,
        "nome": "$_id.nome",
        "total": 1,
        "desconto": {
            "$cond": {"if": {"$gte": ["$total", 10]}, "then": True, "else": False}
        }
    }}
])

writeAJson(resultado, "result1")

