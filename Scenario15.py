# Scenario 15: Online Quiz Score Tracking

# 1. Store quiz scores as list of tuples -> (user, quiz_name, score)
quiz_scores = []

# 2. Set of unique users
users_set = set()

# 3. Dictionary to store average score per user
# Example: {"Alice": 85.5}
avg_scores = {}


def add_score():
    user = input("Enter User Name: ")
    quiz = input("Enter Quiz Name: ")
    score = float(input("Enter Score (0-100): "))

    if score < 0 or score > 100:
        print("Invalid score! Enter 0-100.")
        return

    # Add to list
    quiz_scores.append((user, quiz, score))

    # Add user to set
    users_set.add(user)

    # Update average score
    update_avg_score(user)
    print("Score added successfully!")


def update_avg_score(user):
    total = 0
    count = 0
    for u, q, s in quiz_scores:
        if u == user:
            total += s
            count += 1
    avg_scores[user] = round(total / count, 2)


def show_avg_scores():
    print("\n--- Average Scores per User ---")
    if not avg_scores:
        print("No scores yet!")
    else:
        for user, avg in avg_scores.items():
            print(f"{user}: {avg}")


def show_users():
    print("\n--- All Users ---")
    if not users_set:
        print("No users yet!")
    else:
        print(users_set)


# ---------------- Main Menu ----------------
while True:
    print("\n===== Online Quiz Score Tracking =====")
    print("1. Add Score")
    print("2. Show Average Scores per User")
    print("3. Show All Users")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_score()
    elif choice == "2":
        show_avg_scores()
    elif choice == "3":
        show_users()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
