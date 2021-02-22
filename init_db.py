import src.orm as orm
from src.orm.entities import Author, Book, BookAuthor


def main():
    orm.reinitialize()
    author = Author(firstname="amir")
    author.save()
    b1 = Book(name="b1", author=author)
    b1.save()
    b2 = Book(name="b2", author=author)
    b2.save()
    BookAuthor.insert(author=author, book=b1).execute()
    BookAuthor.insert(author=author, book=b2).execute()


if __name__ == "__main__":
    main()
