# Scenario 10: Online Shopping Cart System

# 1. Store items as tuples -> (item_name, price)
cart_items = []

# 2. Set of unique item names
unique_items = set()

# 3. Dictionary for total price per item
# Example: {"Laptop": 50000, "Mouse": 700}
price_totals = {}


def add_item():
    item = input("Enter Item Name: ")
    price = float(input("Enter Item Price: "))

    # Add to list
    cart_items.append((item, price))

    # Add to set
    unique_items.add(item)

    # Add/Update dictionary
    if item not in price_totals:
        price_totals[item] = 0
    price_totals[item] += price

    print("Item added to cart!")


def display_total_cost():
    print("\n--- Total Cost of Cart ---")
    if len(cart_items) == 0:
        print("Cart is empty!")
    else:
        total = sum(price for _, price in cart_items)
        print(f"Total Cost: ₹{total}")


def list_cart_items():
    print("\n--- Items in Cart ---")
    if len(unique_items) == 0:
        print("No items added yet!")
    else:
        print(unique_items)


# ---------------- Main Menu ----------------
while True:
    print("\n===== Online Shopping Cart System =====")
    print("1. Add Item")
    print("2. Display Total Cost")
    print("3. List Cart Items")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_item()
    elif ch == "2":
        display_total_cost()
    elif ch == "3":
        list_cart_items()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
