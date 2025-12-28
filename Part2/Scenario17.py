import numpy as np

data_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# 1. Convert to NumPy array
data_array = np.array(data_list)

# 2. Reshape to 3×4
reshaped = data_array.reshape(3, 4)

# 3. Extract last column
last_column = reshaped[:, -1]

print("Array:", data_array)
print("Reshaped:", reshaped)
print("Last column:", last_column)
