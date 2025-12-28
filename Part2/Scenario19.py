import numpy as np

temps = np.array([
    22, 21, 20, 19, 18, 20, 22, 25, 28, 30, 32, 34,
    36, 38, 37, 35, 33, 30, 28, 26, 25, 24, 23, 22
])

# 2. Hottest period (12 PM to 4 PM)
hot_period = temps[12:17]

# 3. Morning average (6 AM to 11 AM)
morning_avg = np.mean(temps[6:12])

# 4. Max and Min temperature
max_temp = np.max(temps)
min_temp = np.min(temps)

# 5. Celsius to Fahrenheit
fahrenheit = (temps * 9/5) + 32

print("Hot period temps:", hot_period)
print("Morning average:", morning_avg)
print("Max temp:", max_temp)
print("Min temp:", min_temp)
print("Fahrenheit:", fahrenheit)
