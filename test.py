from peewee import *

db = MySQLDatabase('myscript', user='hoda', password='1234', port=4306)


class Book(Model):
    id = PrimaryKeyField()
    name = CharField()
    author = CharField()

    class Meta:
        database = db


def main():
    print("Hello World!")
    db.connect()
    db.create_tables([Book])
    book = Book(name="B1", author="a1")
    book.save()
    b = Book.select().get()
    print(b.name)


if __name__ == "__main__":
    main()
