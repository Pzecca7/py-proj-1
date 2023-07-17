### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["George Orwell", "J.K Rowling", "Roald Dahl", "Agatha Christie", "Mary Shelley", "Ernest Hemmingway", "William Shakespeare", "Stephen King" ]

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here

my_authors.append("Mark Twain")

print(my_authors)



# Now let's remove an element in the list

# Code here

my_authors.pop()

print(my_authors)



# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here

print(my_authors[2])

# Now slice the list.

# Code here

print(my_authors[3:7])

### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here

my_tuple = ("George Orwell", "J.K Rowling", "Roald Dahl", "Agatha Christie", "Mary Shelley", "Ernest Hemmingway", "William Shakespeare", "Stephen King")

print(my_tuple)

### Step 3 - Sets ###

# Create a set with your authors.

# Code here

my_set = {"George Orwell", "J.K Rowling", "Roald Dahl", "Agatha Christie", "Mary Shelley", "Ernest Hemmingway", "William Shakespeare", "Stephen King"}



# Add a new author to your set.

# Code here

my_set.add("John Grisham")

print(my_set)

# Try adding the same author again, and be sure to print your set.

# Code here

my_set.add("John Grisham")

print(my_set)



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here

for name in my_authors:
    print(name)

for name in my_tuple:
    print(name)

for name in my_set:
    print(name)



