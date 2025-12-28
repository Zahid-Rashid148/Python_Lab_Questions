import numpy as np

img = np.array([
    [20, 40, 60, 80],
    [30, 50, 70, 120],
    [25, 45, 65, 85],
    [35, 55, 75, 95]
])

# 1. Add 50 brightness
bright = img + 50

# 2. First two rows
first_two = img[:2, :]

# 3. Count pixels > 100
count = np.sum(img > 100)

print("Bright: " ,bright)
print("First two rows: ",first_two)
print("Pixels>100: ",count)