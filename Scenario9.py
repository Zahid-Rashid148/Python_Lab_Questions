# Scenario 9: Bus Ticket Booking System

# 1. Store bookings as tuples -> (ticket_id, passenger_name, seat_no)
bookings = []

# 2. Set of booked seats
booked_seats = set()

# 3. Dictionary mapping seat -> passenger
# Example: {"A1": "Ravi"}
seat_passenger_map = {}


def add_booking():
    ticket_id = input("Enter Ticket ID: ")
    passenger = input("Enter Passenger Name: ")
    seat_no = input("Enter Seat Number: ")

    # Check if seat is already booked
    if seat_no in booked_seats:
        print("Seat already booked! Choose another seat.")
        return

    # Add to list of tuples
    bookings.append((ticket_id, passenger, seat_no))

    # Add seat to set
    booked_seats.add(seat_no)

    # Add to seat-passenger dictionary
    seat_passenger_map[seat_no] = passenger

    print("Booking added successfully!")


def check_booked_seats():
    print("\n--- Booked Seats ---")
    if len(booked_seats) == 0:
        print("No seats booked yet!")
    else:
        print(booked_seats)


def list_ticket_details():
    print("\n--- Ticket Details (Seat → Passenger) ---")
    if len(seat_passenger_map) == 0:
        print("No bookings yet!")
    else:
        for seat, name in seat_passenger_map.items():
            print(f"{seat}: {name}")


# ---------------- Main Menu ----------------
while True:
    print("\n===== Bus Ticket Booking System =====")
    print("1. Add Booking")
    print("2. Check Booked Seats")
    print("3. List Ticket Details")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_booking()
    elif ch == "2":
        check_booked_seats()
    elif ch == "3":
        list_ticket_details()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
