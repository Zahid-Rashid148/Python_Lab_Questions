import numpy as np

speed = np.array([40, 42, 45, 47, 50, 48, 46, 49, 51, 53])

# 1. Max and min speeds
maximum = np.max(speed)
minimum = np.min(speed)

# 2. Speeds from second 4 to 8 (index 3 to 7)
mid_speed = speed[3:8]

# 3. Add calibration error +2
corrected_speed = speed + 2
print("Maximum: ",maximum)
print("Minimum: ",minimum)
print("Mid speeds: ",mid_speed)
print("Corrected speed: ",corrected_speed)