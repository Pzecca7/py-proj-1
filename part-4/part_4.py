### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def create_new_book():

#     title = input("What is the title of the book you want to add? ")
#     author = input("Who is the author of the book? ")
#     year = input("what year was this book published ")
#     rating = input("what rating out of 5 would you give this book? ") 
#     pages = input("what is the page count of the book? ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def create_new_book():

#     title = input("What is the title of the book you want to add? ")
#     author = input("Who is the author of the book? ")
#     year = int(input("what year was this book published "))
#     rating = float(input("what rating out of 5 would you give this book? "))
#     pages = int(input("what is the page count of the book? "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary




# print(create_new_book())


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here


def create_new_book():

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

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

book_library = [{

    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "rating": 1.99,
    "pages": 208
},
{

    "title": "FrankenStein",
    "author": "Mary Shelley",
    "year": 1818,
    "rating": 3.77,
    "pages": 280
},
{

    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "rating": 4.11,
    "pages": 328
},
{
    "title": "Fifty Shades of Grey",
    "author": "E.L. James",
    "year": 2011,
    "rating": 0.85,
    "pages": 514
},
{
    "title": "Twilight",
    "author": "Stephenie Meyer",
    "year": 2005,
    "rating": 3.03,
    "pages": 498
},
{
    
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
},
{
    "title": "Harry Potter and the Philosopher's Stone",
    "author": "J.K Rowling",
    "year": 1997,
    "rating": 4.88,
    "pages": 223
},
{
    "title": "The Fellowship of the Ring",
    "author": "J.R.R Tolkien",
    "year": 1954,
    "rating": 3.84,
    "pages": 423
},
{
    "title": "Charlie and the Choclate Factory",
    "author": "Roald Dahl",
    "year": 1964,
    "rating": 3.22,
    "pages": 161
},
{
    "title": "The Odyssey",
    "author": "Homer",
    "year": 1614,
    "rating": 1.83,
    "pages": 541
}
]

def good_book_lookup(book_list):

    for book in book_list:
        if book["rating"] >= 4:
            good_book = (f'{book["title"]} has a rating of {book["rating"]}')
            print(good_book)

good_book_lookup(book_library)

def okay_book_lookup(book_list):
     
     for book in book_list:
        if 2 <= book["rating"] < 4:
            okay_book = (f'{book["title"]} has a rating of {book["rating"]}')
            print(okay_book)
        
okay_book_lookup(book_library)

def bad_book_lookup(book_list):
        
    for book in book_list:
        if book["rating"] < 2:
            bad_book = (f'{book["title"]} has a rating of {book["rating"]}')
            print(bad_book)
            
        
bad_book_lookup(book_library)

def book_information(book_dictionary):
    info_string = (f'Here is all the information about this book: {book_dictionary}')

    return info_string


def show_all_books(book_list):
    for book in book_list:
        print(book_information(book))

# def main_menu(book_sources):
#     active = True

#     while active:
#         choice = input("To add a book, choose 1\nTo see all the books in the library choose 2\nTo look up highly reviewed books choose 3\nTo lookup mixed reviewed books choose 4\nTo lookup poorly reviewed books choose 5\nTo exit, choose 6\n")

#         if choice == "1":
#             book_sources.append(create_new_book())
#         elif choice == "2":
#             print(show_all_books(book_sources))
#         elif choice == "3":
#             print(good_book_lookup())
#         elif choice == "4":
#             print(okay_book_lookup())
#         elif choice == "5":
#             print(bad_book_lookup())
#         elif choice == "6":
#             print("Thanks for using the home library app!")
#             active= False
#         else:
#             print("please Select a valid option.")

# main_menu(book_library)

    
    



### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def main_menu(book_sources):
    active = True

    while active:
        choice = input("To add a book, choose 1\nTo see all the books in the library choose 2\nTo look up highly reviewed books choose 3\nTo lookup mixed reviewed books choose 4\nTo lookup poorly reviewed books choose 5\nTo exit, choose 6\n")

        if choice == "1":
            book_sources.append(create_new_book())
        elif choice == "2":
            show_all_books(book_sources)
        elif choice == "3":
            good_book_lookup(book_sources)
        elif choice == "4":
            okay_book_lookup(book_sources)
        elif choice == "5":
            bad_book_lookup(book_sources)
        elif choice == "6":
            print("Thanks for using the home library app!")
            active= False
        else:
            print("please Select a valid option.")

main_menu(book_library)