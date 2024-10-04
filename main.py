import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MJ123",
        database="Library",
        auth_plugin="mysql_native_password"
    )
    
cursor=db.cursor()

# Taking important inputs from user.



a=str(input("Enter your user name:"))

v=int(input("Enter your user ID:"))

c=str(input("Is user a premium member (yes or no):"))
c=c.lower()

cursor.execute("SELECT ID FROM user WHERE ID = %s", (v,))
existing_user = cursor.fetchone()

if existing_user:
    print(f"User with ID {v} already exists.")
else:
    # Insert new user if ID doesn't exist
    sql = "INSERT INTO user(ID, Name, Membership) VALUES (%s, %s, %s)"
    val = (v, a, c)
    cursor.execute(sql, val)
    db.commit()
    print(f"User {a} added successfully.")
    




n=str(input("You want to borrow a book (yes or no):"))
n=n.lower()

l=str(input("You want to return a book (yes or no):"))
l=l.lower()


# variable for verification.
e="yes"

f="no"

#Main Library Funtion which perform different task.
    
class Library:
    
    #Funtion for adding the books.
    def add(self, name, author):
    # Check if the book already exists
        cursor.execute("SELECT 1 FROM books WHERE Name = %s AND Author = %s", (name, author)) 
        existing_book = cursor.fetchone()
        
        
        cursor.execute("SELECT Book_name FROM borrowed_books WHERE Book_name = %s", (name,)) 
        existing_bbook=cursor.fetchone()
    
        if existing_book:
            print(f"Book with {name} by {author} already exists.")  
        elif existing_bbook:
                print(f"Book with {name} by {author} already exists.")
        else:
            # Insert new book if it doesn't exist
            sql = "INSERT INTO books(Name,Author) VALUES(%s,%s)"
            val = (name, author)  
            cursor.execute(sql, val)
            db.commit()
            print(f"Book {name} by {author} added successfully.")


            
        
    #Funtion for removing the books. 
    def remove(self, name):
        
        cursor.execute("SELECT Name FROM books WHERE Name = %s", (name,))
        existing_book = cursor.fetchone()
    
        if existing_book:
            cursor.execute("DELETE FROM books WHERE Name = %s", (name,))
            db.commit()
            print(f"Book {name} removed successfully.")
        else:
            print("Book not found in the library.")
            
       
    
    #Funtion for displaying the books.
    def display(self):
        cursor.execute("SELECT * FROM books")  # Fetch all books from the table
        books_from_db = cursor.fetchall()

        if books_from_db:
            print("Available Books:")
            for book in books_from_db:
                name = book[0]  # Assuming Name is the first column
                author = book[1]  # Assuming Author is the second column
                print(f" - {name} by {author}")
        else:
            print("No books found in the library.")
            
    #Funtion for borrowing the books for premium member.    
    def borrow(self):
        print(" Thanks for being a premium member, you can borrow 5 books")
        g = int(input("Enter Number of books you want to borrow: "))

        if g <= 5:
            for i in range(g):
                name = str(input("Enter the name of the book you want to borrow: "))

                # Check if the book exists in the database
                cursor.execute("SELECT 1 FROM books WHERE Name = %s", (name,))
                existing_book = cursor.fetchone()

                if existing_book:
                    # Book exists, proceed with borrowing
                    sql2 = ("INSERT INTO borrowed_books(ID, Book_name) VALUES(%s, %s)")
                    val1 = (v, name)
                    cursor.execute(sql2, val1)
                    db.commit()

                    # Delete the book from the database
                    cursor.execute("DELETE FROM books WHERE Name = %s", (name,))
                    db.commit()

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

                cursor.execute("SELECT 1 FROM books WHERE Name = %s", (name,))
                existing_book = cursor.fetchone()

                if existing_book:
                    # Book exists, proceed with borrowing
                    sql2 = ("INSERT INTO borrowed_books(ID, Book_name) VALUES(%s, %s)")
                    val1 = (v, name)
                    cursor.execute(sql2, val1)
                    db.commit()

                    # Delete the book from the database
                    cursor.execute("DELETE FROM books WHERE Name = %s", (name,))
                    db.commit()

                    print(f"Book '{name}' borrowed by {a}.")
                else:
                    print(f"Book '{name}' not found in the library.")
        else:
            print("You are not allowed to borrow more than 3 books")

             
             
    #Funtion for displaying the books borrowed.    
    def display_borrowed_books(self):
        cursor.execute("SELECT * FROM borrowed_books") 
        bbooks_from_db = cursor.fetchall()

        if bbooks_from_db:
            print("Borrowed Books Are:")
            for book in bbooks_from_db:
                id = book[0]  
                name = book[1]  
                print(f" - {id} by {name}")
        else:
            print("No books found in the Borrowed books.")
            
    
    #Funtion for returning the books.
    def return_book(self):
        x=int(input("Enter Number of books you want to return:"))
        
        for i in range(x):
            
            name=input("Enter name of the book you want to return:")   
            author=input("Enter name of the author:")
                     
            cursor.execute("SELECT 1 FROM borrowed_books WHERE Book_name = %s", (name,))
            existing_book = cursor.fetchone()
            
            if existing_book:
                    sql3=("Delete from borrowed_books where ID=%s and Book_name=%s")
                    val2=(v,name)
                    cursor.execute(sql3,val2)
                    db.commit()
                    
                    sql4= ("INSERT INTO books(Name,Author) VALUES(%s,%s)")
                    val4=(name,author)
                    cursor.execute(sql4,val4)
                    db.commit()
                    
                    print(f"Book '{name}' returned successfully.")
            else:
                print(f"Book '{name}' not found in borrowed books.")
                
        
# Object decleration for the class.

lib=Library()


# Calling of add funtion from library class.
lib.add("xy","z")
lib.add("ab","c")
lib.add("de","x")
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
    

lib.display_borrowed_books()


# Calling of return_books funtion from library class
if l==e:
    lib.return_book()





# Calling of display_borrowed_books funtion from library class
lib.display_borrowed_books()

