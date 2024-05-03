class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def remove_book(self, book):


        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from the library.")
        else:
            print(f"Book '{book}' not found in the library.")

    def display_books(self):
        if self.books:
            print("Books available in the library:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")

# Example usage

my_library = Library()

my_library.add_book("viking kings")
my_library.add_book("The monk who sold his ferrari")
my_library.add_book("Jay shetty")
my_library.add_book("Game of thrones")


my_library.display_books()

my_library.remove_book("To Kill a Mockingbird")

my_library.display_books()
