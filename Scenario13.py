# Scenario 13: Employee Salary Updater

salary_updates = []            # List of tuples (emp_id, name, salary)
emp_ids = set()                # Set of emp_id for uniqueness
salary_dict = {}               # Dictionary {name: last_salary}


def add_or_update_salary():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Salary: "))

    # Add to list as tuple
    salary_updates.append((emp_id, name, salary))

    # Add emp_id to the set
    emp_ids.add(emp_id)

    # Update latest salary in dictionary
    salary_dict[name] = salary

    print("\nSalary Updated Successfully!\n")


def show_salary_sheet():
    print("\n====== Salary Sheet ======")
    for name, salary in salary_dict.items():
        print(f"{name} → ₹{salary}")
    print("==========================\n")


# ---------- Main Menu ----------
while True:
    print("=== Employee Salary Updater ===")
    print("1. Add/Update Salary")
    print("2. Show Salary Sheet")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_or_update_salary()
    elif choice == "2":
        show_salary_sheet()
    elif choice == "3":
        print("Exiting Program...")
        break
    else:
        print("Invalid choice! Try again.\n")
