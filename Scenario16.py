# Scenario 16: Car Rental Booking System

# 1. Store bookings as list of tuples -> (booking_id, car_model, customer)
bookings = []

# 2. Set to track booked car models
booked_models = set()

# 3. Dictionary to store car-wise customers
# Example: {"Sedan": ["Ravi", "Anita"]}
car_customers = {}


def add_booking():
    booking_id = input("Enter Booking ID: ")
    car_model = input("Enter Car Model: ")
    customer = input("Enter Customer Name: ")

    # Add to bookings list
    bookings.append((booking_id, car_model, customer))

    # Add car model to set
    booked_models.add(car_model)

    # Add customer to dictionary under the car model
    if car_model not in car_customers:
        car_customers[car_model] = []
    car_customers[car_model].append(customer)

    print("Booking added successfully!")


def show_booked_models():
    print("\n--- Booked Car Models ---")
    if not booked_models:
        print("No bookings yet!")
    else:
        print(booked_models)


def show_car_customers():
    print("\n--- Car-wise Customers ---")
    if not car_customers:
        print("No bookings yet!")
    else:
        for model, customers in car_customers.items():
            print(f"{model}: {customers}")


# ---------------- Main Menu ----------------
while True:
    print("\n===== Car Rental Booking System =====")
    print("1. Add Booking")
    print("2. Show Booked Car Models")
    print("3. Show Car-wise Customers")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_booking()
    elif choice == "2":
        show_booked_models()
    elif choice == "3":
        show_car_customers()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
