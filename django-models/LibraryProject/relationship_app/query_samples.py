import os
import django

# Setup Django environment (only needed if running as standalone script)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # Replace with your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "John Doe"  # You can change the name as needed
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    librarian = Librarian.objects.get(library__name=library_name)
    return librarian


# --- Sample usage ---
if __name__ == "__main__":
    print("Books by author 'John Doe':")
    for book in get_books_by_author('John Doe'):
        print(book.title)

    print("\nBooks in library 'Central Library':")
    for book in get_books_in_library('Central Library'):
        print(book.title)

    print("\nLibrarian for 'Central Library':")
    librarian = get_librarian_for_library('Central Library')
    print(librarian.name)
