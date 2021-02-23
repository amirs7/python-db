from src.orm.entities import Book


def main():
    book = Book.select().get()
    print(book.name)


if __name__ == "__main__":
    main()
