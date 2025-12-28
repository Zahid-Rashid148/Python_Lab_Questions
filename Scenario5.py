# Scenario 5: Employee Attendance Recorder

# 1. Attendance logs stored as list of tuples -> (emp_id, emp_name, status)
attendance_logs = []

# 2. Set to track unique employee IDs
employee_ids = set()

# 3. Dictionary to track total presents per employee -> {"Ravi": 20, "Asha": 22}
present_count = {}

# Set to track today's absent employees
absent_today = set()


def add_attendance():
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    status = input("Enter Status (Present/Absent): ").strip().lower()

    # Add employee ID to unique set
    employee_ids.add(emp_id)

    # Add log to tuple list
    attendance_logs.append((emp_id, emp_name, status))

    # Count present
    if status == "present":
        if emp_name not in present_count:
            present_count[emp_name] = 0
        present_count[emp_name] += 1
    elif status == "absent":
        absent_today.add(emp_name)
    else:
        print("Invalid status entered (use Present/Absent)")


def show_present_count():
    print("\n--- Total Presents Per Employee ---")
    for name, count in present_count.items():
        print(f"{name}: {count}")


def show_absent_today():
    print("\n--- Employees Absent Today ---")
    if len(absent_today) == 0:
        print("No one is absent today!")
    else:
        print(absent_today)


# ---------------- Main Menu ----------------
while True:
    print("\n===== Employee Attendance Recorder =====")
    print("1. Add Attendance Entry")
    print("2. Show Number of Presents Per Employee")
    print("3. Show Employees Absent Today")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_attendance()
    elif ch == "2":
        show_present_count()
    elif ch == "3":
        show_absent_today()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
