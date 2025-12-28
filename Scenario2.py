# ------------------------------------------------------------
# Online Grocery Store Inventory System
# ------------------------------------------------------------

# 1. Store products as list of tuples → (item_name, price, quantity)
products = []

# 2. Set to track all available item names
item_names = set()

# 3. Dictionary to map item name → total inventory value
inventory_value = {}


# ------------------------------------------------------------
# Function: Add new item
# ------------------------------------------------------------
def add_item():
    print("\n--- Add New Item ---")
    
    item_name = input("Enter item name: ")
    price = float(input("Enter price per unit: "))
    quantity = int(input("Enter quantity: "))

    # Add tuple to products list
    products.append((item_name, price, quantity))

    # Add item name to set
    item_names.add(item_name)

    print("Item added successfully!")


# ------------------------------------------------------------
# Function: Calculate inventory value for each item
# ------------------------------------------------------------
def calculate_inventory_value():
    print("\n--- Inventory Value Calculation ---")

    if not products:
        print("No items available!")
        return

    inventory_value.clear()  # Reset before recalculation

    for item_name, price, quantity in products:
        total = price * quantity

        # If item appears multiple times, add values
        if item_name in inventory_value:
            inventory_value[item_name] += total
        else:
            inventory_value[item_name] = total

    # Display results
    for name, total in inventory_value.items():
        print(f"{name}: ₹{total}")


# ------------------------------------------------------------
# Function: Display low-stock items (quantity < 5)
# ------------------------------------------------------------
def display_low_stock():
    print("\n--- Low Stock Items (Quantity < 5) ---")

    found = False
    for item_name, price, quantity in products:
        if quantity < 5:
            print(f"{item_name}: Only {quantity} left!")
            found = True

    if not found:
        print("All items sufficiently stocked.")


# ------------------------------------------------------------
# MENU-DRIVEN LOOP
# ------------------------------------------------------------
while True:
    print("\n===============================")
    print(" Online Grocery Inventory")
    print("===============================")
    print("1. Add New Item")
    print("2. Calculate Inventory Value")
    print("3. Display Low-Stock Items")
    print("4. Exit")
    print("===============================")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        calculate_inventory_value()
    elif choice == '3':
        display_low_stock()
    elif choice == '4':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice, enter between 1–4.")
