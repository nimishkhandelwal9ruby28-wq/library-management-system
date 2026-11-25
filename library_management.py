import os
import ast
from pathlib import Path

# Vishwa Bharati Public School Dwarka
#
# Basic Library System

# ----------------------------
# Sample Data and Structures
# ----------------------------

userList = []        # List of user dictionaries
transactionList = [] # Borrow/Return records

userCount = 1
bookCount = 61   # Start from 61 since 60 books are pre-added
transCount = 1


#----------------------------
#Admin login
#----------------------------
def login():
    """Authenticate using credentials supplied through environment variables."""
    print("---- Login ----")
    # Demo defaults let the project run immediately.
    # Override these with environment variables for a private local setup.
    expected_username = os.getenv("LIBRARY_ADMIN_USERNAME", "admin")
    expected_password = os.getenv("LIBRARY_ADMIN_PASSWORD", "1234")

    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == expected_username and password == expected_password:
        print("Login successful!\\n")
        return True
    print("Invalid login.")
    return False


# ----------------------------
# Available Books (Pre-added)
# ----------------------------
titles_and_authors = [
    ("The Great Gatsby", "F. Scott Fitzgerald", "classic"),
    ("To Kill a Mockingbird", "Harper Lee", "classic"),
    ("1984", "George Orwell", "dystopian"),
    ("Pride and Prejudice", "Jane Austen", "romance"),
    ("The Catcher in the Rye", "J.D. Salinger", "classic"),
    ("The Hobbit", "J.R.R. Tolkien", "fantasy"),
    ("Moby-Dick", "Herman Melville", "adventure"),
    ("Jane Eyre", "Charlotte Brontë", "romance"),
    ("The Lord of the Rings", "J.R.R. Tolkien", "fantasy"),
    ("The Alchemist", "Paulo Coelho", "philosophy"),
    ("Animal Farm", "George Orwell", "dystopian"),
    ("The Book Thief", "Markus Zusak", "fiction"),
    ("The Chronicles of Narnia", "C.S. Lewis", "fantasy"),
    ("Brave New World", "Aldous Huxley", "dystopian"),
    ("Wuthering Heights", "Emily Brontë", "romance"),
    ("Frankenstein", "Mary Shelley", "horror"),
    ("Little Women", "Louisa May Alcott", "classic"),
    ("Fahrenheit 451", "Ray Bradbury", "dystopian"),
    ("The Kite Runner", "Khaled Hosseini", "fiction"),
    ("Life of Pi", "Yann Martel", "fiction"),
    ("The Fault in Our Stars", "John Green", "romance"),
    ("The Shining", "Stephen King", "horror"),
    ("Gone Girl", "Gillian Flynn", "mystery"),
    ("The Da Vinci Code", "Dan Brown", "mystery"),
    ("Percy Jackson: The Lightning Thief", "Rick Riordan", "fantasy"),
    ("A Tale of Two Cities", "Charles Dickens", "classic"),
    ("The Invisible Man", "H.G. Wells", "fiction"),
    ("Dracula", "Bram Stoker", "horror"),
    ("The Secret Garden", "Frances Hodgson Burnett", "classic"),
    ("Great Expectations", "Charles Dickens", "classic"),
    ("The Time Machine", "H.G. Wells", "fiction"),
    ("The Picture of Dorian Gray", "Oscar Wilde", "classic"),
    ("David Copperfield", "Charles Dickens", "classic"),
    ("Around the World in 80 Days", "Jules Verne", "adventure"),
    ("War and Peace", "Leo Tolstoy", "classic"),
    ("Crime and Punishment", "Fyodor Dostoevsky", "classic"),
    ("Les Misérables", "Victor Hugo", "classic"),
    ("The Odyssey", "Homer", "classic"),
    ("The Iliad", "Homer", "classic"),
    ("Meditations", "Marcus Aurelius", "philosophy"),
    ("Don Quixote", "Miguel de Cervantes", "classic"),
    ("The Brothers Karamazov", "Fyodor Dostoevsky", "classic"),
    ("Anna Karenina", "Leo Tolstoy", "classic"),
    ("The Count of Monte Cristo", "Alexandre Dumas", "adventure"),
    ("The Three Musketeers", "Alexandre Dumas", "adventure"),
    ("A Christmas Carol", "Charles Dickens", "classic"),
    ("Treasure Island", "Robert Louis Stevenson", "adventure"),
    ("Gulliver’s Travels", "Jonathan Swift", "adventure"),
    ("Robinson Crusoe", "Daniel Defoe", "adventure"),
    ("Ulysses", "James Joyce", "classic"),
    ("Dubliners", "James Joyce", "classic"),
    ("Lolita", "Vladimir Nabokov", "fiction"),
    ("Beloved", "Toni Morrison", "fiction"),
    ("The Sound and the Fury", "William Faulkner", "fiction"),
    ("Of Mice and Men", "John Steinbeck", "classic"),
    ("The Grapes of Wrath", "John Steinbeck", "classic"),
    ("Slaughterhouse-Five", "Kurt Vonnegut", "fiction"),
    ("Catch-22", "Joseph Heller", "fiction"),
    ("On the Road", "Jack Kerouac", "fiction")
]

bookList = []
i = 0
for title, author, category in titles_and_authors:
    book = {
        "id": "B" + str(i + 1),
        "title": title,
        "author": author,
        "category": category,
        "available": True
    }
    bookList.append(book)
    i += 1


# ----------------------------
# Helper Functions
# ----------------------------

def makeUserId():
    global userCount
    uid = "U" + str(userCount)
    userCount += 1
    return uid

def makeBookId():
    global bookCount
    bid = "B" + str(bookCount)
    bookCount += 1
    return bid

def makeTransId():
    global transCount
    tid = "T" + str(transCount)
    transCount += 1
    return tid 

def printLine():
    print("-" * 50)

# ----------------------------
# File Save & Load
# ----------------------------

DATA_DIR = Path(__file__).resolve().parent
USERS_FILE = DATA_DIR / "users.txt"
BOOKS_FILE = DATA_DIR / "books.txt"
TRANSACTIONS_FILE = DATA_DIR / "transactions.txt"


def _read_records(path):
    """Read one Python-literal dictionary per line; ignore blank lines."""
    if not path.exists():
        return []
    records = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                record = ast.literal_eval(line)
                if isinstance(record, dict):
                    records.append(record)
    return records


def saveData():
    with USERS_FILE.open("w", encoding="utf-8") as file:
        for user in userList:
            file.write(repr(user) + "\\n")

    with BOOKS_FILE.open("w", encoding="utf-8") as file:
        for book in bookList:
            file.write(repr(book) + "\\n")

    with TRANSACTIONS_FILE.open("w", encoding="utf-8") as file:
        for transaction in transactionList:
            file.write(repr(transaction) + "\\n")


def loadData():
    global userList, bookList, transactionList
    global userCount, bookCount, transCount

    userList = _read_records(USERS_FILE)
    saved_books = _read_records(BOOKS_FILE)
    if saved_books:
        bookList = saved_books
    transactionList = _read_records(TRANSACTIONS_FILE)

    if userList:
        userCount = max(int(user["id"][1:]) for user in userList) + 1
    if bookList:
        bookCount = max(int(book["id"][1:]) for book in bookList) + 1
    if transactionList:
        transCount = max(int(transaction["id"][1:]) for transaction in transactionList) + 1


# ----------------------------
# User Management
# ----------------------------

def addUser():
    print("Add New User")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    address = input("Enter Address: ")
    uid = makeUserId()
    user = {"id": uid, "name": name, "age": age, "address": address, "borrowed": []}
    userList.append(user)
    saveData()
    print("User added successfully with ID:", uid)

def viewUsers():
    printLine()
    print("List of Users")
    for u in userList:
        print("ID:", u["id"], "| Name:", u["name"], "| Borrowed Books:", len(u["borrowed"]))
    printLine()

def deleteUser():
    uid = input("Enter User ID to Delete: ")
    for u in userList:
        if u["id"] == uid:
            userList.remove(u)
            saveData()
            print("User deleted.")
            return
    print("User not found.")

def editUser():
    uid = input("Enter User ID to edit: ")
    for u in userList:
        if u["id"] == uid:
            print("Editing User:", u["name"])
            new_name = input("Enter new name (leave blank to keep same): ")
            new_age = input("Enter new age (leave blank to keep same): ")
            new_address = input("Enter new address (leave blank to keep same): ")

            if new_name: u["name"] = new_name
            if new_age: u["age"] = new_age
            if new_address: u["address"] = new_address

            saveData()
            print("User details updated successfully!")
            return
    print("User not found.")


# ----------------------------
# Book Management
# ----------------------------

def addBook():
    print("Add New Book")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    year = input("Enter Year: ")
    cat = input("Enter Category: ").lower()
    bid = makeBookId()
    book = {
        "id": bid,
        "title": title,
        "author": author,
        "year": year,
        "category": cat,
        "available": True
    }
    bookList.append(book)
    saveData()
    print("Book added successfully with ID:", bid)

def viewBooks():
    printLine()
    print("List of Books")
    for b in bookList:
        status = "Available" if b["available"] else "Not Available"
        print("ID:", b["id"], "|", b["title"], "by", b["author"], "|", b["category"], "|", status)
    printLine()

def deleteBook():
    bid = input("Enter Book ID to Delete: ")
    for b in bookList:
        if b["id"] == bid:
            bookList.remove(b)
            saveData()
            print("Book deleted.")
            return
    print("Book not found.")

def searchBook():
    keyword = input("Enter book title or author: ").lower()
    found = 0
    for b in bookList:
        if keyword in b["title"].lower() or keyword in b["author"].lower():
            print(f'{b["id"]} | {b["title"]} by {b["author"]}')
            found += 1
    if found == 0:
        print("No book found.")


# ----------------------------
# Borrow and Return
# ----------------------------

def borrowBook():
    uid = input("Enter User ID: ")
    bid = input("Enter Book ID: ")

    user = None
    book = None
    for u in userList:
        if u["id"] == uid:
            user = u
            break

    for b in bookList:
        if b["id"] == bid:
            book = b
            break

    if user is None:
        print("User not found.")
        return
    if book is None:
        print("Book not found.")
        return
    if not book["available"]:
        print("Book is already borrowed.")
        return

    book["available"] = False
    user["borrowed"].append(bid)

    tid = makeTransId()
    transactionList.append({"id": tid, "user_id": uid, "book_id": bid, "status": "borrowed"})

    saveData()
    print(f'Book "{book["title"]}" borrowed successfully by {user["name"]}.')

def returnBook():
    uid = input("Enter User ID: ")
    bid = input("Enter Book ID: ")

    for u in userList:
        if u["id"] == uid and bid in u["borrowed"]:
            u["borrowed"].remove(bid)
            for b in bookList:
                if b["id"] == bid:
                    b["available"] = True
                    book_title = b["title"]
                    break

            transactionList.append({"id": makeTransId(), "user_id": uid, "book_id": bid, "status": "returned"})
            saveData()
            print(f'Book "{book_title}" returned successfully by {u["name"]}.')
            return

    print("Record not found.")


#------------------------------
#Recommend
#-----------------------------
def recommendBook():
    genre = input("Enter preferred genre (classic / fantasy / mystery / philosophy): ").lower()
    if "fantasy" in genre:
        print("You might like 'The Hobbit' or 'The Lord of the Rings'.")
    elif "mystery" in genre:
        print("Try 'Gone Girl' or 'The Da Vinci Code'.")
    elif "philosophy" in genre:
        print("Try 'Meditations' or 'The Alchemist'.")
    else:
        print("You might enjoy classics like 'Pride and Prejudice' or '1984'.")


#----------------------------
#Statistics
#----------------------------

def showStats():
    total_books = len(bookList)
    total_users = len(userList)
    printLine()
    print("Library Statistics:")
    print("Total Books:", total_books)
    print("Total Users:", total_users)
    printLine()


#-----------------------------------------
#Books Borrowed by a Particular User
#-----------------------------------------
def viewBorrowedBooks():
    uid = input("Enter User ID: ")
    for u in userList:
        if u["id"] == uid:
            if not u["borrowed"]:
                print("No books borrowed.")
            else:
                print(f"Books borrowed by {u['name']}:")
                for bid in u["borrowed"]:
                    for b in bookList:
                        if b["id"] == bid:
                            print(f'- {b["title"]} by {b["author"]}')
            return
    print("User not found.")


#----------------------------
#Search user
#----------------------------
def searchUser():
    keyword = input("Enter name or ID: ").lower()
    for u in userList:
        if keyword in u["name"].lower() or keyword == u["id"].lower():
            print("User Found:", u['id'], "|", u['name'], "| Borrowed:", len(u['borrowed']), "books")
            return
    print("User not found.")


#-----------------------------
#FEEDBACK
#-----------------------------
def feedback():
    printLine()
    fb = input("Enter your feedback for the library: ")
    with open("feedback.txt", "a") as f:
        f.write(fb + "\n")
    print("Thank you for your feedback!")


#-----------------------------
#Rate a book
#-----------------------------
def rateBook():
    book_title = input("Enter book title to rate: ")
    for b in bookList:
        if b["title"].lower() == book_title.lower():
            rating = int(input("Give rating (1-5): "))
            b["rating"] = rating
            print(f"Thanks for rating '{b['title']}' {rating}/5")
            return
    print("Book not found.")

# ----------------------------
# Main Menu
# ----------------------------

def mainMenu():
    print("=====================================")
    print()
    print("Library Management System")
    print("Developed by: NIMISH KHANDELWAL and RISHANK TOMAR")
    print()
    print("=======================================")
    while True:
        printLine()
        print("1. Add User")
        print("2. View Users")
        print("3. Delete User")
        print("4. Add Book")
        print("5. View Books")
        print("6. Delete Book")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Search Book")
        print("10.Book Recommendation ")
        print("11. Edit User")
        print("12.Statistics")
        print("13.Books Borrowed by a Particular User")
        print("14.Search a user ")
        print("15.Feedback")
        print("16.Rate a book")
        print("0. Exit")
        printLine()
        choice = input("Enter your choice: ")

        if choice == "1":
            addUser()
        elif choice == "2":
            viewUsers()
        elif choice == "3":
            deleteUser()
        elif choice == "4":
            addBook()
        elif choice == "5":
            viewBooks()
        elif choice == "6":
            deleteBook()
        elif choice == "7":
            borrowBook()
        elif choice == "8":
            returnBook()
        elif choice == "9":
            searchBook()
        elif choice=="10":
            recommendBook()
        elif choice == "11":
            editUser()
        elif choice =="12":
            showStats()
        elif choice=="13":
            viewBorrowedBooks()
        elif choice=="14":
            searchUser()
        elif choice=="15":
            feedback()
        elif choice=="16":
            rateBook()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if login():
    loadData()
    mainMenu()
else:
    print("Access denied.")
 