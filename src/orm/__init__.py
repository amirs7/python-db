from .database import instance, config
from .entities import Author
from .entities import Book
from .entities import BookAuthor

print("Database Config: ", config)
instance.init(database.name, **config)
instance.connect()


def reinitialize():
    instance.drop_tables([Book, Author, BookAuthor])
    instance.create_tables([Book, Author, BookAuthor])
    BookAuthor.delete().execute()
    Book.delete().execute()
    Author.delete().execute()
