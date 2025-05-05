#11. Class Methods
#Assignment:
#Create a class Book with a class variable total_books. Add a class method increment_book_count()
# to increase the count when a new book is added.

class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Increment book count when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"Total books: {cls.total_books}")

# Example usage
book1 = Book("Python Programming")
book2 = Book("Data Science Essentials")
book3 = Book("Machine Learning Basics")

# Display total books
Book.display_total_books()
