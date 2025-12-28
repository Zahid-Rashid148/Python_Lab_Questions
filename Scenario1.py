# ------------------------------------------------------------
# Library Book Tracking System (Menu Driven Program)
# ------------------------------------------------------------

# 1. List to store book records (book_id, book_title, student_name)
books = []

# 2. Set to maintain unique book IDs
unique_book_ids = set()

# 3. Dictionary to store books borrowed by each student
student_books = {}


# ------------------------------------------------------------
# Function to add a borrowed book record
# ------------------------------------------------------------
def add_book_record():
    print("\n--- Add Borrowed Book Record ---")
    
    book_id = int(input("Enter Book ID: "))
    book_title = input("Enter Book Title: ")
    student_name = input("Enter Student Name: ")

    # Check duplicate book ID
    if book_id in unique_book_ids:
        print("Error: Book ID already exists! Record not added.")
        return

    # Add tuple to list
    books.append((book_id, book_title, student_name))

    # Add id to set
    unique_book_ids.add(book_id)

    # Add book title under student
    if student_name not in student_books:
        student_books[student_name] = []
    student_books[student_name].append(book_title)

    print("Book record added successfully!")


# ------------------------------------------------------------
# Function to display student-wise borrowed books
# ------------------------------------------------------------
def display_student_books():
    print("\n--- Student-wise Borrowed Books ---")
    if not student_books:
        print("No records found!")
        return

    for student, book_list in student_books.items():
        print(f"{student}: {book_list}")


# ------------------------------------------------------------
# Function to show all unique book IDs
# ------------------------------------------------------------
def show_unique_book_ids():
    print("\n--- Unique Book IDs ---")
    if not unique_book_ids:
        print("No book IDs available!")
    else:
        print(unique_book_ids)


# ------------------------------------------------------------
# MAIN MENU LOOP
# ------------------------------------------------------------
while True:
    print("\n==============================")
    print("   Library Tracking System")
    print("==============================")
    print("1. Add Borrowed Book Record")
    print("2. Display Student-wise Books")
    print("3. Show Unique Book IDs")
    print("4. Exit")
    print("==============================")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_book_record()
    elif choice == '2':
        display_student_books()
    elif choice == '3':
        show_unique_book_ids()
    elif choice == '4':
        print("Thank you! Exiting program...")
        break
    else:
        print("Invalid choice! Please enter 1-4.")
