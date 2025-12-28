# Scenario 8: Gym Membership Attendance Tracker

# 1. Attendance entries stored as tuples -> (member_id, name, status)
attendance_entries = []

# 2. Set to track unique member IDs
member_ids = set()

# 3. Dictionary to count total presents per member
present_count = {}   # Example: {"Amit": 12, "Sara": 15}

# Set to track today's absentees
absentees_today = set()


def add_attendance():
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")
    status = input("Enter Status (Present/Absent): ").strip().lower()

    # Add to unique ID set
    member_ids.add(member_id)

    # Add attendance log
    attendance_entries.append((member_id, name, status))

    # Count presence
    if status == "present":
        if name not in present_count:
            present_count[name] = 0
        present_count[name] += 1

    elif status == "absent":
        absentees_today.add(name)

    else:
        print("Invalid status! Use Present/Absent")


def show_attendance_count():
    print("\n--- Total Attendance Count ---")
    if len(present_count) == 0:
        print("No attendance records yet!")
        return

    for name, count in present_count.items():
        print(f"{name}: {count} days present")


def list_absentees():
    print("\n--- Absentees Today ---")
    if len(absentees_today) == 0:
        print("Nobody is absent today!")
    else:
        print(absentees_today)


# ---------------- Main Menu ----------------
while True:
    print("\n===== Gym Membership Attendance Tracker =====")
    print("1. Add Attendance")
    print("2. Show Attendance Count")
    print("3. List Absentees Today")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_attendance()
    elif ch == "2":
        show_attendance_count()
    elif ch == "3":
        list_absentees()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
