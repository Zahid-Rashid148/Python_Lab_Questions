import numpy as np

sales = np.array([
    [23, 19, 35],
    [12, 15, 18],
    [30, 28, 40],
    [14, 17, 20]
])

# 1. Total sales per category (row-wise sum)
category_total = np.sum(sales, axis=1)
print("Category total: ",category_total)

# 2. Total sales per day (column-wise)
day_total = np.sum(sales, axis=0)
print("Day total: ",day_total)

# 3. Revenue per day
price = np.array([120, 250, 400, 150])
revenue = price @ sales     # dot product
print("Revenue: " ,revenue)