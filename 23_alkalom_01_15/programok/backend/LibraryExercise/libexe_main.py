from o_23_alkalom_01_15.backend.LibraryExercise.Book.Book import Book
from o_23_alkalom_01_15.backend.LibraryExercise.Library.Library import Library


def main():
    # Usage example
    library = Library('data/books.json')

    # Add a book
    new_book = Book('The Great Gatsby', 'F. Scott Fitzgerald', 1925, '9780743273565')
    library.add_book(new_book)

    another_book = Book('The Great Gatsby 2', 'F. Scott Fitzgerald', 1945, '1080743273565')
    library.add_book(another_book)

    de_book = Book('Ja', 'Auf Deutsche Bitte', 1989, '6565074337774')
    library.add_book(de_book)

    # List books
    library.list_books()
    print("end list\n")

    # Sort books by year
    library.sort_books_by_year()
    library.list_books()
    print("end sorting\n")

    # Get books by author
    books_by_author = library.get_books_by_author('F. Scott Fitzgerald')
    for book in books_by_author:
        print(f'{book.title} by {book.author}')

    print("end books by author\n")


main()
