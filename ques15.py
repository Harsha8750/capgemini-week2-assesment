class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __add__(self, other):
        if isinstance(other, Book):
            return BookSeries([self, other])
        else:
            raise ValueError("Can only concatenate Book objects")

class BookSeries:
    def __init__(self, books):
        self.books = books

    def display_series(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")


book1 = Book("The Fellowship of the Ring", "J.R.R. Tolkien")
book2 = Book("The Two Towers", "J.R.R. Tolkien")

book_series = book1 + book2
book_series.display_series()
