# ------------------------------------------------------------
# Classroom Gradebook Manager
# ------------------------------------------------------------

# 1. Dictionary storing students → list of scores
grades = {
    "Alice": [90, 85],
    "Bob": [70, 80]
}

# 3. Set of all students
students = set(grades.keys())


# ------------------------------------------------------------
# Function: Add new (student, score) pair
# ------------------------------------------------------------
def add_score():
    print("\n--- Add Student Score ---")
    
    name = input("Enter student name: ")
    score = int(input("Enter score: "))

    # Add new student if not present
    if name not in grades:
        grades[name] = []
        students.add(name)

    # Add the score
    grades[name].append(score)

    print("Score added successfully!")


# ------------------------------------------------------------
# Function: Average score per student
# ------------------------------------------------------------
def calculate_averages():
    print("\n--- Average Score Per Student ---")

    for student, score_list in grades.items():
        if score_list:  # avoid divide by zero
            avg = sum(score_list) / len(score_list)
            print(f"{student}: {avg:.2f}")
        else:
            print(f"{student}: No scores available")


# ------------------------------------------------------------
# Function: Find the highest scorer (using tuple comparison)
# ------------------------------------------------------------
def highest_scorer():
    print("\n--- Highest Scorer ---")

    highest = None   # will store tuple → (max_score, student_name)

    for student, score_list in grades.items():
        if score_list:
            max_score = max(score_list)
            # tuple comparison → higher score wins; tie breaks by student name
            current = (max_score, student)

            if highest is None or current > highest:
                highest = current

    if highest:
        print(f"Highest Scorer: {highest[1]} with score {highest[0]}")
    else:
        print("No scores available!")


# ------------------------------------------------------------
# MAIN MENU LOOP
# ------------------------------------------------------------
while True:
    print("\n==============================")
    print("   Classroom Gradebook Menu")
    print("==============================")
    print("1. Add New Score")
    print("2. Calculate Average Scores")
    print("3. Show Highest Scorer")
    print("4. Exit")
    print("==============================")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_score()
    elif choice == '2':
        calculate_averages()
    elif choice == '3':
        highest_scorer()
    elif choice == '4':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, enter 1-4.")
