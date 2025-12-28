# Scenario 18: Eventify Workshop Registration System

# 1. Store participant details as list of tuples -> (participant_id, name, workshop_name)
participants = []

# 2. Set to track unique participant IDs
participant_ids = set()

# 3. Dictionary to group participants by workshop
workshop_dict = {
    "Python Basics": [],
    "Data Science": [],
    "AI Introduction": []
}


def add_participant():
    participant_id = input("Enter Participant ID: ")
    
    # Check for duplicate ID
    if participant_id in participant_ids:
        print("Duplicate ID! Entry ignored.")
        return

    name = input("Enter Participant Name: ")
    print("Select Workshop:")
    print("1. Python Basics")
    print("2. Data Science")
    print("3. AI Introduction")
    choice = input("Enter choice (1-3): ")

    if choice == "1":
        workshop = "Python Basics"
    elif choice == "2":
        workshop = "Data Science"
    elif choice == "3":
        workshop = "AI Introduction"
    else:
        print("Invalid choice!")
        return

    # Add to list of tuples
    participants.append((participant_id, name, workshop))

    # Add to participant ID set
    participant_ids.add(participant_id)

    # Add to workshop dictionary
    workshop_dict[workshop].append(name)

    print("Participant added successfully!")


def show_participant_report():
    print("\n====== Participant Report ======")
    print(f"Total Workshops: {len(workshop_dict)}\n")

    print("Number of participants in each workshop:")
    for workshop, names in workshop_dict.items():
        print(f"{workshop}: {len(names)} participants")

    print("\nAll unique participant IDs:")
    print(participant_ids)
    print("===============================\n")


# ---------------- Main Menu ----------------
while True:
    print("===== Eventify Workshop Registration =====")
    print("1. Add Participant")
    print("2. Show Participant Report")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_participant()
    elif choice == "2":
        show_participant_report()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
