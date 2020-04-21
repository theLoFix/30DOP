import input_functions as inf
from files_mgmt import create_book_table 


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """



def menu():
    create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            inf.prompt_add_book()
        elif user_input == 'l':
            inf.list_books()
        elif user_input == 'r':
            inf.prompt_read_book()
        elif user_input == 'd':
            inf.prompt_delete_book()

        user_input = input(USER_CHOICE)