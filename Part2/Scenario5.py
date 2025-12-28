import numpy as np

hr = np.array([72, 75, 78, 80, 76, 74, 79, 82])

# 1. Extract readings from hour 3 to 6
extract = hr[2:6]

# 2. Average heart rate
avg_hr = np.mean(hr)

# 3. Convert bpm scale (multiply by 0.8)
converted = hr * 0.8

print("Extracted: ",extract)
print("Average: ",avg_hr)
print("Converted: ",converted)