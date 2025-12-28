import numpy as np

temps = np.arange(1, 16).reshape(3, 5)
  # 1. reshape 15 values into 3x5

# 2. Temperatures of City 2 (row index 1)
city2 = temps[1, :]

# 3. Subtract correction factors
correction = np.array([1, 0, 2, 1, 0])
corrected = temps - correction
print(corrected)