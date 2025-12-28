import numpy as np

data = np.random.randint(1, 50, (3, 100))   # Example accelerometer data
print("Data: ",data)

# 1. Extract y-axis readings (row index 1)
y_readings = data[1, :]

# 2. Mean of each axis
means = np.mean(data, axis=1)

# 3. Readings from index 20 to 40
cut = data[:, 20:41]
print("Y-readings: ",y_readings)
print("Means: ",means)
print("Cut: ",cut)