# Scenario 7: Restaurant Menu Rating System

# 1. Store ratings as list of tuples -> (item_name, rating)
ratings = []

# 2. Set of available / rated food items
food_items = set()

# 3. Dictionary to store average rating per item
average_ratings = {}   # Example: {"Pizza": 4.3, "Burger": 3.8}


def add_rating():
    item = input("Enter Food Item Name: ")
    rating = float(input("Enter Rating (1 to 5): "))

    # Validate rating
    if rating < 1 or rating > 5:
        print("Invalid rating! Please enter between 1 and 5.")
        return

    # Add rating as tuple
    ratings.append((item, rating))

    # Add item to set
    food_items.add(item)

    print("Rating added successfully!")

    # Update average rating
    update_average_rating(item)


def update_average_rating(item):
    total = 0
    count = 0

    for it, r in ratings:
        if it == item:
            total += r
            count += 1

    average_ratings[item] = round(total / count, 2)


def show_average_ratings():
    print("\n--- Average Ratings per Food Item ---")
    if len(average_ratings) == 0:
        print("No ratings yet!")
        return

    for item, avg in average_ratings.items():
        print(f"{item}: ⭐ {avg}")


def list_all_items():
    print("\n--- All Items Rated ---")
    if len(food_items) == 0:
        print("No items rated yet!")
    else:
        print(food_items)


# ---------------- Main Menu ----------------
while True:
    print("\n===== Restaurant Menu Rating System =====")
    print("1. Add Rating")
    print("2. Show Average Ratings")
    print("3. List All Items Rated")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_rating()
    elif ch == "2":
        show_average_ratings()
    elif ch == "3":
        list_all_items()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
