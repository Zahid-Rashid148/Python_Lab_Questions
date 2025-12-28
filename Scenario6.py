# Scenario 6: Student Sports Registration System

# 1. List of registrations stored as tuples → (student_id, name, sport)
registrations = []

# 2. Set of unique student IDs
student_ids = set()

# 3. Dictionary to group students by sport
# Example: { "Football": ["Ravi", "Imran"], "Cricket": ["Asha"] }
sport_groups = {}


def add_registration():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    sport = input("Enter Sport Name: ")

    # Add to set of unique IDs
    student_ids.add(student_id)

    # Add to list of tuples
    registrations.append((student_id, name, sport))

    # Add to sport-wise dictionary
    if sport not in sport_groups:
        sport_groups[sport] = []
    sport_groups[sport].append(name)

    print("Registration added successfully!")


def show_sport_wise():
    print("\n--- Sport-wise Participants ---")
    for sport, names in sport_groups.items():
        print(f"{sport}: {names}")


def view_unique_ids():
    print("\n--- All Unique Student IDs ---")
    print(student_ids)


# ---------------- Main Menu ----------------
while True:
    print("\n===== Student Sports Registration System =====")
    print("1. Add Registration")
    print("2. Show Sport-wise Participants")
    print("3. View All Unique Student IDs")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_registration()
    elif ch == "2":
        show_sport_wise()
    elif ch == "3":
        view_unique_ids()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
