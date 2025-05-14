
"""
11. Class Methods
Assignment:
Create a class Book with a class variable total_books. 
Add a class method increment_book_count() to increase the count when a new book is added.

"""
# Create the book class
class Book:
    # Create the class variable
    total_books = 0
    def __init__(self , title:str , author:str ) -> None:
        self.title = title
        self.author = author
        Book.increment_book_count()
    
    # Define the class method
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        
# Try to access the class variable and method by instance
book : Book = Book("My Succed Life" , "Muhammad Saad Ahmed")
print(f"The {book.author} has written total {book.total_books} books")

# Try to acccess class methods and variable without instance
Book.increment_book_count()
print(f"The {book.author} has written total {Book.total_books} books")
