my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

book_library = [{
    
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
    "title": "Charlie and the Choclate Facrtory",
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


# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_information(book_dictionary):
    info_string = (f'Here is all the information about this book: {book_dictionary}')

    return info_string

print(book_information(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def book_title(book_dictionary):

    title_string = (f'The title of the book is {book_dictionary["title"]}')
    return title_string

print(book_title(my_book))

def book_author(book_dictionary):

    author_string = (f'The author of the book is {book_dictionary["author"]}')
    return author_string

print(book_author(my_book))

def year_published(book_dictionary):

    published_string = (f'The book was published in {book_dictionary["year"]}')
    return published_string

print(year_published(my_book))

def book_rating(book_dictionary):

    rating_string = (f'The rating of the book is {book_dictionary["rating"]}')
    return rating_string

print(book_rating(my_book))

def book_length(book_dictionary):

    pages_string = (f'The length of the book is {book_dictionary["pages"]}')
    return pages_string

print(book_length(my_book))



# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

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