
import files_mgmt as file

def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    insert_book(name, author)


def insert_book(name, author):
    books = file.get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    file.save_all_books(books)


def list_books():
    for book in file.get_all_books():
        read = 'YES' if book['read'] == '1' else 'NO'  # book[3] will be a falsy value (0) if not read
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')

    mark_book_as_read(name)


def mark_book_as_read(name):
    books = file.get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    file.save_all_books(books)


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')

    delete_book(name)


def delete_book(name):
    books = file.get_all_books()
    books = [book for book in books if book['name'] != name]
    file.save_all_books(books)
