import numpy as np


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author

class Library:
    def __init__(self):
        """initialize an empty library"""
        self.collections = []

    def __getitem__(self, key):
        return self.collections.__getitem__(key)

    def __len__(self):
        return self.collections.__len__()

    def by_author(self, specified_author): # sorting method
        search_result = [i for i in self.collections if i.author==specified_author]
        if len(search_result)==0:
            raise KeyError("No item with matching author!")
        return search_result

    def by_title(self, specified_title):
        search_result = [i for i in self.collections if i.title==specified_title]
        if len(search_result)==0:
            raise KeyError("No item with matching title!")
        return search_result

    def add_book(self, book_or_title, author=None):
        """Add either:
        1. a book, OR
        2. a an entry by providing the (title, author)."""
        if author is None:
            assert isinstance(book_or_title, Book), "Use case 1: provide"
            new_book = book_or_title
        else:
            assert isinstance(book_or_title, str) and isinstance(author, str), "Use case 2: 1"
            new_book = Book(book_or_title, author)
        self.collections.append(new_book)

    @property
    def titles(self):
        return [book.title for book in self.collections]

    @property
    def authors(self):
        return list(set(book.author for book in self.collections))