# Taking important inputs from user.

a=str(input("Enter your name:"))

c=str(input("Are you a premium member (yes or no):"))
c=c.lower()

n=str(input("You want to borrow a book (yes or no):"))
n=n.lower()

l=str(input("You want to return a book (yes or no):"))
l=l.lower()


# variable for verification.
e="yes"

f="no"

#Main Library Funtion which perform different task.
    
class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}
    
    #Funtion for adding the books.
    def add(self, name, author):
        self.books[name] = author
        
    #Funtion for removing the books. 
    def remove(self, name):
        if name in self.books:
            del self.books[name]
            print("Book removed.")
        else:
            print("Book not found in the library.")
    
    #Funtion for displaying the books.
    def display(self):
        if self.books:
            print("Available Books:")
            for name, author in self.books.items():
                print(f" - {name} by {author}")
        else:
            print("No books found in the library.")
            
    #Funtion for borrowing the books for premium member.    
    def borrow(self):
        print(" Thanks for bening premium member you can borrow 5 books")
        g=int(input("Enter Number of books you want to borrow:"))
         
        if g <= 5:
            for i in range(g):
                name = str(input("Enter the name of the book you want to borrow: "))

                if name in self.books:
                    if a not in self.borrowed_books:
                        self.borrowed_books[a] = []
                    self.borrowed_books[a].append(name)

                    del self.books[name]
                    print(f"Book '{name}' borrowed by {a}.")
                else:
                    print(f"Book '{name}' not found in the library.")
        else:
            print("You are not allowed to borrow more than 5 books")
             
    #Funtion for borrowing the books for non-premium member.
    def borrow2(self):
        print(" As you are not a premium member you can borrow 3 books")
        t=int(input("Enter Number of books you want to borrow:"))
         
        if t <= 3:
            for i in range(t):
                name = str(input("Enter the name of the book you want to borrow: "))

                if name in self.books:
                    if a not in self.borrowed_books:
                        self.borrowed_books[a] = []
                    self.borrowed_books[a].append(name)

                    del self.books[name]
                    print(f"Book '{name}' borrowed by {a}.")
                else:
                    print(f"Book '{name}' not found in the library.")
        else:
            print("You are not allowed to borrow more than 3 books")

             
             
    #Funtion for displaying the books borrowed.    
    def display_borrowed_books(self):
        if self.borrowed_books: 
            print("Borrowed Books:")
            for member, books in self.borrowed_books.items():
                print(f"{member}:")
                for book in books:
                    print(f"  - {book}")
        else:
            print("No books are currently borrowed.")
    
        #Funtion for returning the books.
    def return_book(self):
        h=int(input("Enter Number of books you want to return:"))
        for i in range(h):
            name=input("Enter name of the book you want to return:")
            author=input("Enter name of the author:")
            self.books[name] = author
            for member, books in self.borrowed_books.items():
                if name in books:
                    books.remove(name)
                    print(f"Book '{name}' returned successfully.")
                    break
            else:
                print(f"Book '{name}' not found in borrowed books.")
                
        
# Object decleration for the class.

lib=Library()


# Calling of add funtion from library class.
lib.add("xy","z")
lib.add("ab","c")
lib.add("de","xf")
lib.add("fg","h")
lib.add("jk","l")

# Calling of remove funtion from library class.
lib.remove("fg")

# Calling of display funtion from library class.
lib.display()

# Verifiying if the member is a premium member or not
if n==e: 
    if c == e:
        lib.borrow()
    elif c==f:
        lib.borrow2()
    else:
        print("Invalid input")
else:
    print("Moving ahead")
    
lib.display()

# Calling of return_books funtion from library class
if l==e: 
    if n == e:
        lib.return_book()
    else:
        print("You have not borrowed any book that can be returned")





# Calling of display_borrowed_books funtion from library class
lib.display_borrowed_books()

