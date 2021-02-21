from peewee import *
from .. import database
from .book import Book
from .author import Author


class BookAuthor(Model):
    book = ForeignKeyField(Book)
    author = ForeignKeyField(Author, backref='books')

    class Meta:
        database = database.instance
