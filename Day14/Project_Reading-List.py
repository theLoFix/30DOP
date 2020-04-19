# Day 14 Project: Reading List

# The brief
# For this project the application needs to have the following functionality:

# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
# Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
# Users should be able to search for a specific book by providing a book title.
# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).

reading_list = []

menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search for a book
- 'q' to quit

What would you like to do? """

selected_option = input(menu_prompt).strip().lower()


def add_book():
    print("You selected 'a'.")

    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    with open("Day14\\books.csv","a") as file:
        file.write(f"{title};{author};{year}\n")

def get_all_books():
    books=[]

    with open("Day14\\books.csv", "r") as file:
        for book in file:
            title,author,year = book.strip().split(";")

            books.append({
                "title": title,
                "author": author,
                "year": year
            })
    return books


def search_book():
    reading_list = get_all_books()
    matching_books = []

    search_term = input("Please enter a book title to search for: ").strip().lower()

    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)

    return matching_books


def show_books(books):
    print()
    for book in books:
        title, author, year = book.values()
        print(f"{title}, by {author} ({year})")
    print()


while True:
    selected_option = input(menu_prompt).strip().lower()

    if selected_option == "q":
        break
    elif selected_option == "a":
        add_book()
    elif selected_option == "l":
        reading_list = get_all_books()
        if reading_list:
            show_books(reading_list)
        else:
            print("Your reading list is empty.")
    elif selected_option == "s":
        matching_books = search_book()
        if matching_books:
            show_books(matching_books)
        else:
            print("Sorry, we didn't find any books for that search term.")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")	
