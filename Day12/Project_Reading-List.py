# Day 12 Project: Reading List

# The brief
# For this project the application needs to have the following functionality:

# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# The program should store information about all of these books in a Python list.
# Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.
# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).

reading_list = []

menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

What would you like to do? """

selected_option = input(menu_prompt).strip().lower()


def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()
    
    reading_list.append({
        "title": title,
        "author": author,
        "year": year
    })


def show_books():
    for book in reading_list:
        title, author, year = book.values()
        print(f"{title}, by {author} ({year})")

while True:
    selected_option = input(menu_prompt).strip().lower()

    if selected_option == "q":
        break
    elif selected_option == "a":
        add_book()
    elif selected_option == "l":
        if reading_list:
            show_books()
        else:
            print("Your reading list is empty.")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")	
