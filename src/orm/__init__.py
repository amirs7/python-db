from . import database
from .entities import Author
from .entities import Book
from .entities import BookAuthor

db = database.instance
print("Database Config: ", database.config)
db.init(database.name, **database.config)
db.connect()


def initialize():
    db.drop_tables([Book, Author, BookAuthor])
    db.create_tables([Book, Author, BookAuthor])
    BookAuthor.delete().execute()
    Book.delete().execute()
    Author.delete().execute()
