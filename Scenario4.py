# Scenario 4: Movie Ticket Booking Tracker

# 1. List of bookings stored as tuples -> (booking_id, movie_name, seat_no)
bookings = []

# 2. Set to maintain booked seat numbers (to avoid duplicates)
booked_seats = set()

# 3. Dictionary to store movie-wise seats
movie_bookings = {}   # Example: { "Movie A": ["A1", "A2"], "Movie B": ["B3"] }


def add_booking():
    booking_id = input("Enter Booking ID: ")
    movie_name = input("Enter Movie Name: ")
    seat_no = input("Enter Seat Number: ")

    # Check duplicate seat
    if seat_no in booked_seats:
        print("❌ Seat already booked! Choose another seat.")
        return

    # Add to tuple list
    bookings.append((booking_id, movie_name, seat_no))

    # Add seat to set
    booked_seats.add(seat_no)

    # Add to dictionary
    if movie_name not in movie_bookings:
        movie_bookings[movie_name] = []
    movie_bookings[movie_name].append(seat_no)

    print("✔ Booking added successfully!")


def list_bookings_movie_wise():
    print("\n---- Movie-wise Bookings ----")
    for movie, seats in movie_bookings.items():
        print(f"{movie} → {seats}")


def show_all_booked_seats():
    print("\nAll booked seats:", booked_seats)


# ---------- Main Menu ----------
while True:
    print("\n==== Movie Ticket Booking Tracker ====")
    print("1. Add Booking")
    print("2. List Bookings Movie-wise")
    print("3. Show All Booked Seats")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_booking()
    elif ch == "2":
        list_bookings_movie_wise()
    elif ch == "3":
        show_all_booked_seats()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")