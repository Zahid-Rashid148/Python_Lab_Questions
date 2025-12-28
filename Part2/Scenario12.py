import numpy as np

prices = np.array([80, 120, 150, 60, 200, 100])

# 1. Apply flat ₹5 discount
discounted = prices - 5

# 2. Most expensive and cheapest item
max_price = np.max(prices)
min_price = np.min(prices)

# 3. Items priced above ₹100
above_100 = prices[prices > 100]

print("Discounted prices:", discounted)
print("Most expensive item:", max_price)
print("Cheapest item:", min_price)
print("Items above ₹100:", above_100)
