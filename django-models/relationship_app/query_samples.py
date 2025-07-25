from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author (e.g., "Jane Doe")
def books_by_author():
    try:
        author = Author.objects.get(name="Jane Doe")
        books = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print("Author not found.")

# Query 2: List all books in a library (e.g., "Central Library")
def books_in_library():
    try:
        library = Library.objects.get(name="Central Library")
        books = library.books.all()
        print(f"Books in {library.name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print("Library not found.")

# Query 3: Retrieve the librarian for a library (e.g., "Central Library")
def librarian_for_library():
    try:
        library = Library.objects.get(name="Central Library")
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library.name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Library or Librarian not found.")

# Call all functions for demonstration
if __name__ == "__main__":
    books_by_author()
    books_in_library()
    librarian_for_library()

