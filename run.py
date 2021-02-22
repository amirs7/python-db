import src.orm as orm
from src.orm.entities import Author, Book, BookAuthor


def main():
    book = Book.select().get()
    print(book.name)


if __name__ == "__main__":
    main()
