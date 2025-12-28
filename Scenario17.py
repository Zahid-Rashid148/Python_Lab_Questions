# Scenario 17: Event Feedback Analyzer

# 1. Store feedback as list of tuples -> (participant, score)
feedback_records = []

# 2. Set of participants
participants_set = set()

# 3. Dictionary for score classification: "High" or "Low"
# Example: {"Alice": "High"}
score_classification = {}


def add_feedback():
    participant = input("Enter Participant Name: ")
    score = float(input("Enter Feedback Score (0-10): "))

    if score < 0 or score > 10:
        print("Invalid score! Enter 0-10.")
        return

    # Add to list
    feedback_records.append((participant, score))

    # Add to participants set
    participants_set.add(participant)

    # Classify score
    if score >= 7:
        score_classification[participant] = "High"
    else:
        score_classification[participant] = "Low"

    print("Feedback added successfully!")


def show_participants():
    print("\n--- All Participants ---")
    if not participants_set:
        print("No feedback yet!")
    else:
        print(participants_set)


def show_score_classification():
    print("\n--- Score Classification ---")
    if not score_classification:
        print("No feedback yet!")
    else:
        for participant, classification in score_classification.items():
            print(f"{participant}: {classification}")


# ---------------- Main Menu ----------------
while True:
    print("\n===== Event Feedback Analyzer =====")
    print("1. Add Feedback")
    print("2. Show Participants")
    print("3. Show Score Classification")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_feedback()
    elif choice == "2":
        show_participants()
    elif choice == "3":
        show_score_classification()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
