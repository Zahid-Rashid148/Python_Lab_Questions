import numpy as np

warehouse_A = np.array([50, 30, 20, 60])
warehouse_B = np.array([40, 35, 25, 50])

# 1. Total inventory
total_inventory = warehouse_A + warehouse_B

# 2. Highest total quantity item
max_item = np.max(total_inventory)

# 3. Items where A > B
more_in_A = total_inventory[warehouse_A > warehouse_B]

print("Total inventory:", total_inventory)
print("Highest quantity:", max_item)
print("More in Warehouse A:", more_in_A)
