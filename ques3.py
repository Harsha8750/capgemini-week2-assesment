#You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.

class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

    def book_details(self):
        print(f'The name of the book is: {self.title}')
        print(f'The author of the book is: {self.author}')
        print(f'The isbn of the book is: {self.isbn}')

title=input("Enter the title of the book: ")
author=input("Enter the author of the book is: ")
isbn=int(input("Enter the isbn of the book: "))
bk=Book(title,author,isbn)
bk.book_details()