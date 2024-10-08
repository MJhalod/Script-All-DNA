from flask import Flask,render_template,url_for,request,jsonify
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



# user_name=str(input("Enter your user name:"))

# user_id=int(input("Enter your user ID:"))

# user_membership=str(input("Is user a premium member (yes or no):"))
# c=user_membership.lower()


    


# variable for verification.
verification1="yes"

verification2="no"

    
    #Main Library Funtion which perform different task.
    
class Library:
        
        def add_member(self, user_name, user_id, membership):
            
            cursor.execute("SELECT ID FROM user WHERE ID = %s", (user_id,))
            existing_user = cursor.fetchone()

            if existing_user:
                print(f"User with ID {user_id} already exists.")
            else:
                # Insert new user if ID doesn't exist
                sql = "INSERT INTO user(ID, Name, Membership) VALUES (%s, %s, %s)"
                val = (user_id, user_name, membership)
                cursor.execute(sql, val)
                db.commit()
                print(f"User {user_name} added successfully.")
            
    
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
            
            cursor.execute("SELECT * FROM books") 
            detail= cursor.fetchall()
            global details
            details=dict(detail)
            # cursor.execute("SELECT * FROM books")  # Fetch all books from the table
            # books_from_db = cursor.fetchall()

            # if books_from_db:
            #     print("Available Books:")
            #     for book in books_from_db:
            #         name = book[0]  # Assuming Name is the first column
            #         author = book[1]  # Assuming Author is the second column
            #         print(f" - {name} by {author}")
            # else:
            #     print("No books found in the library.")
            
            
    #Funtion for borrowing the books for premium member.    
        def borrow(self):
            print("Thanks for being a premium member, you can borrow 5 books")
            number_borrowP = int(input("Enter Number of books you want to borrow: "))

            if number_borrowP <= 5:
                for i in range(number_borrowP):
                    name = str(input("Enter the name of the book you want to borrow: "))

                    # Check if the book exists in the database
                    cursor.execute("SELECT 1 FROM books WHERE Name = %s", (name,))
                    existing_book = cursor.fetchone()

                    if existing_book:
                        # Book exists, proceed with borrowing
                        sql1 = ("INSERT INTO borrowed_books(ID, Book_name) VALUES(%s, %s)")
                        val1 = (user_id, name)
                        cursor.execute(sql1, val1)
                        db.commit()

                        # Delete the book from the database
                        cursor.execute("DELETE FROM books WHERE Name = %s", (name,))
                        db.commit()

                        print(f"Book '{name}' borrowed by {user_name}.")
                    else:
                        print(f"Book '{name}' not found in the library.")
            else:
                print("You are not allowed to borrow more than 5 books")

             
    #Funtion for borrowing the books for non-premium member.
        def borrow2(self):
            print("As you are not a premium member you can borrow 3 books")
            number_borrowNP=int(input("Enter Number of books you want to borrow:"))
         
            if number_borrowNP <= 3:
                for i in range(number_borrowNP):
                    name = str(input("Enter the name of the book you want to borrow: "))

                    cursor.execute("SELECT 1 FROM books WHERE Name = %s", (name,))
                    existing_book = cursor.fetchone()

                    if existing_book:
                        # Book exists, proceed with borrowing
                        sql2 = ("INSERT INTO borrowed_books(ID, Book_name) VALUES(%s, %s)")
                        val2 = (user_id, name)
                        cursor.execute(sql2, val2)
                        db.commit()

                        # Delete the book from the database
                        cursor.execute("DELETE FROM books WHERE Name = %s", (name,))
                        db.commit()

                        print(f"Book '{name}' borrowed by {user_name}.")
                    else:
                        print(f"Book '{name}' not found in the library.")
            else:
                print("You are not allowed to borrow more than 3 books")

                  
    #Funtion for displaying the books borrowed.    
        def display_borrowed_books(self,userid):
            cursor.execute("SELECT * FROM borrowed_books where ID=%s",(userid,)) 
            detail= cursor.fetchall()
            
            print(detail)
            if detail:
                for book in detail:
                    id = book[0]  
                    name = book[1]  
                    borrow={id:name}
                    global borrow_detail
                    borrow_detail=borrow
                print(borrow)
                    
            # else: item = next((item for item in items if item["id"] == item_id), None)
            #     print("You have not borrowed any books.")
            #     return False
            
    
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
                    val3=(user_id,name)
                    cursor.execute(sql3,val3)
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
    
    
app = Flask(__name__)


@app.route("/display",methods = ["GET"])
def display():
    lib.display()
    return jsonify(details)

@app.route("/displayborrow/<int:user_id>",methods = ["GET"])
def displayborrow(user_id):
    lib.display_borrowed_books(user_id)
    a=len(borrow_detail)
    print(a)
    return jsonify(borrow_detail)
        


if(__name__ == "__main__"):
    app.run(debug=True)
    