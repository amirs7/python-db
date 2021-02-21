from peewee import *

db = MySQLDatabase('myscript', user='hoda', password='1234')


class Author(Model):
    id = PrimaryKeyField()
    firstname = CharField()

    class Meta:
        database = db


class Book(Model):
    id = PrimaryKeyField()
    name = CharField()

    class Meta:
        database = db


class BookAuthor(Model):
    book = ForeignKeyField(Book)
    author = ForeignKeyField(Author, backref='books')

    class Meta:
        database = db


def main():
    print("Hello World!")
    db.connect()
    db.drop_tables([Book, Author, BookAuthor])
    db.create_tables([Book, Author, BookAuthor])
    BookAuthor.delete().execute()
    Book.delete().execute()
    Author.delete().execute()
    author = Author(firstname="amir")
    author.save()
    b1 = Book(name="B1", author=author)
    b1.save()
    b2 = Book(name="B2", author=author)
    b2.save()
    BookAuthor.insert(author=author, book=b1).execute()
    BookAuthor.insert(author=author, book=b2).execute()
    for book_entry in author.books:
        print(book_entry.book.name)


if __name__ == "__main__":
    main()
