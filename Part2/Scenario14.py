import numpy as np

grid = np.array([
    [30, 32, 34],
    [35, 36, 33],
    [31, 29, 28]
])

# 1. Second row
second_row = grid[1]

# 2. Third column
third_column = grid[:, 2]

# 3. Maximum temperature
max_temp = np.max(grid)

print("Second row:", second_row)
print("Third column:", third_column)
print("Max temperature:", max_temp)
