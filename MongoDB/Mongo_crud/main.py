from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database("db","livros")

db.create(1,"Clean Code","Robert C. Martin", 2008, 31.0)
db.create(2,"Harry Potter and the Philosopher's Stone","J.K. Rowling", 1997, 27.0)
db.create(3,"Wuthering Heights","Emily Bronte", 1847, 40.0)

# db.update(2,35.0)
# db.delete(1)

livros = db.read()

writeAJson(livros,"livros")

