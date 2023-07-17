### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

def create_new_book(book_source):

    title = input("What is the title of the book you want to add? ")
    author = input("Who is the author of the book? ")
    try:
        year = int(input("What year was this book published? "))
    except:
        year = int(input("Please type a number for the year. "))
    try:
        rating = float(input("What rating out of 5 would you give this book? "))
    except:
        rating = float(input("Please type a number (including decimals) for the rating."))
    try:
        pages = int(input("What is the page count of the book? "))
    except:
        pages = int(input("What is the page count of the book? "))


    with open(book_source, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

# create_new_book("library.txt")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def get_books_from_library(book_source):
    book_list = []

    with open(book_source, "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")
            new_book = {
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)

            }

            book_list.append(new_book)
    
    return book_list

print(get_books_from_library("library.txt"))

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

def good_book_lookup(book_source):

    for book in book_source:
        if book["rating"] >= 4:
            good_book = (f'{book["title"]} has a rating of {book["rating"]}')
            print(good_book)


def okay_book_lookup(book_source):
     
     for book in book_source:
        if 2 <= book["rating"] < 4:
            okay_book = (f'{book["title"]} has a rating of {book["rating"]}')
            print(okay_book)
        


def bad_book_lookup(book_source):
        
    for book in book_source:
        if book["rating"] < 2:
            bad_book = (f'{book["title"]} has a rating of {book["rating"]}')
            print(bad_book)
            
        

def book_information(book_dictionary):
    info_string = (f'Here is all the information about this book: {book_dictionary}')

    return info_string


def show_all_books(book_list):
    for book in book_list:
        print(book_information(book))

def main_menu(book_source):
    active = True

    while active:
        choice = input("To add a book, choose 1\nTo see all the books in the library choose 2\nTo look up highly reviewed books choose 3\nTo lookup mixed reviewed books choose 4\nTo lookup poorly reviewed books choose 5\nTo exit, choose 6\n")

        if choice == "1":
            (create_new_book(book_source))
        elif choice == "2":
            show_all_books(get_books_from_library(book_source))
        elif choice == "3":
            good_book_lookup(get_books_from_library(book_source))
        elif choice == "4":
            okay_book_lookup(get_books_from_library(book_source))
        elif choice == "5":
            bad_book_lookup(get_books_from_library(book_source))
        elif choice == "6":
            print("Thanks for using the home library app!")
            active= False
        else:
            print("please Select a valid option.")


if __name__ == "__main__":
    main_menu("library.txt")


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

