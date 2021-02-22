import unittest

from src.orm import Author


class TestStringMethods(unittest.TestCase):

    def test_load_author(self):
        author = Author.select().where(Author.firstname == 'amir').get()
        self.assertEqual(author.firstname, 'amir')
        self.assertCountEqual([book_entry.book.name for book_entry in author.books], ['B1', 'B2'])


if __name__ == '__main__':
    unittest.main()
