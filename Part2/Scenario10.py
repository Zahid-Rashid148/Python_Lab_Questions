import numpy as np

# Weekly sales data
sales = np.array([1200, 1450, 1600, 1320])

# 1. Apply 10% increase using broadcasting
increased_sales = sales * 1.10

# 2. Compute total monthly sales
total_sales = np.sum(sales)

# 3. Extract Week 2 and Week 3 sales
week2_week3 = sales[1:3]

print("Increased Sales:", increased_sales)
print("Total Monthly Sales:", total_sales)
print("Week 2 & Week 3 Sales:", week2_week3)
