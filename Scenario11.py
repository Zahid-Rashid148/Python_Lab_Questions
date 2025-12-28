# Scenario 11: Library Late Fee Calculator

# 1. Store return data -> (student, book, days_late)
late_records = []

# 2. Set to track all unique students
students = set()

# 3. Dictionary to store total late days per student
# Example: {"Anita": 12}
late_days_total = {}


def add_late_record():
    student = input("Enter Student Name: ")
    book = input("Enter Book Name: ")
    days_late = int(input("Enter Days Late: "))

    # Store tuple
    late_records.append((student, book, days_late))

    # Add to students set
    students.add(student)

    # Update dictionary total
    if student not in late_days_total:
        late_days_total[student] = 0
    late_days_total[student] += days_late

    print("Late record added!")


def show_total_late_days():
    print("\n--- Total Late Days per Student ---")
    if len(late_days_total) == 0:
        print("No records yet!")
        return

    for student, days in late_days_total.items():
        print(f"{student}: {days} days late")


def show_students_with_late_returns():
    print("\n--- Students with Late Returns ---")
    if len(students) == 0:
        print("No students have late returns!")
    else:
        print(students)


# ---------------- Main Menu ----------------
while True:
    print("\n===== Library Late Fee Calculator =====")
    print("1. Add Late Record")
    print("2. Show Total Late Days per Student")
    print("3. Show Students with Late Returns")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_late_record()
    elif ch == "2":
        show_total_late_days()
    elif ch == "3":
        show_students_with_late_returns()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
