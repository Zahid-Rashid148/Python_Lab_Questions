import numpy as np

sales = np.array([1200, 1450, 1600, 1320])

# 1. Apply 10% increase
increased = sales * 1.10

# 2. Total monthly sales
total_sales = np.sum(sales)

# 3. Extract Week 2 & Week 3
mid_weeks = sales[1:3]

print("Increased: ",increased)
print("Total sales: ",total_sales)
print("Mid weeks: ",mid_weeks)