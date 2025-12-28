# Scenario 14: Movie Rating Collector

# 1. Store ratings as list of tuples -> (movie, rating)
ratings = []

# 2. Set of movies
movies_set = set()

# 3. Dictionary to store average rating per movie
# Example: {"Avatar": 4.5}
avg_ratings = {}


def add_rating():
    movie = input("Enter Movie Name: ")
    rating = float(input("Enter Rating (1-5): "))

    if rating < 1 or rating > 5:
        print("Invalid rating! Enter 1 to 5.")
        return

    # Add to list
    ratings.append((movie, rating))

    # Add to set
    movies_set.add(movie)

    # Update average rating
    update_avg_rating(movie)
    print("Rating added successfully!")


def update_avg_rating(movie):
    total = 0
    count = 0
    for m, r in ratings:
        if m == movie:
            total += r
            count += 1
    avg_ratings[movie] = round(total / count, 2)


def show_avg_ratings():
    print("\n--- Average Ratings ---")
    if not avg_ratings:
        print("No ratings yet!")
    else:
        for movie, avg in avg_ratings.items():
            print(f"{movie}: ⭐ {avg}")


def show_movies():
    print("\n--- All Rated Movies ---")
    if not movies_set:
        print("No movies rated yet!")
    else:
        print(movies_set)


# ---------------- Main Menu ----------------
while True:
    print("\n===== Movie Rating Collector =====")
    print("1. Add Rating")
    print("2. Show Average Ratings")
    print("3. Show All Movies")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_rating()
    elif choice == "2":
        show_avg_ratings()
    elif choice == "3":
        show_movies()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
