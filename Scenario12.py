# Scenario 12: Course Enrollment System

# 1. Store enrollments as tuples -> (roll_no, name, course)
enrollments = []

# 2. Set of unique roll numbers
roll_numbers = set()

# 3. Dictionary: course -> list of student names
# Example: {"Python": ["Anil", "Sneha"]}
course_map = {}


def add_enrollment():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course Name: ")

    # Add to list
    enrollments.append((roll, name, course))

    # Add roll number to set
    roll_numbers.add(roll)

    # Update course-wise dictionary
    if course not in course_map:
        course_map[course] = []
    course_map[course].append(name)

    print("Enrollment Added Successfully!")


def show_course_wise():
    print("\n--- Course-wise Enrollment List ---")
    if len(course_map) == 0:
        print("No enrollments yet!")
    else:
        for course, students in course_map.items():
            print(f"{course}: {students}")


def show_total_unique_students():
    print("\n--- Total Unique Students ---")
    print(f"Total Students Enrolled: {len(roll_numbers)}")


# ---------------- Main Menu ----------------
while True:
    print("\n===== Course Enrollment System =====")
    print("1. Add Enrollment")
    print("2. Show Course-wise List")
    print("3. Show Total Unique Students")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_enrollment()
    elif ch == "2":
        show_course_wise()
    elif ch == "3":
        show_total_unique_students()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
