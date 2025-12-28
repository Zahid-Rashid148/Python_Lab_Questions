import numpy as np

steps = np.array([4200, 5800, 7500, 8200, 6900, 10200, 9800])

# 1. Steps array is created above

# 2. Weekend steps (6th & 7th elements)
weekend_steps = steps[-2:]

# 3. Average steps for the week
avg_steps = np.mean(steps)

# 4. Calories burned (steps * 0.04)
calories = steps * 0.04

print(weekend_steps)
print(avg_steps)
print(calories)