from dotenv import load_dotenv
from src.orm import database
from src.orm.entities import Author, Book, BookAuthor

db = database.instance
load_dotenv()


def main():
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
