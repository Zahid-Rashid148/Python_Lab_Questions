import numpy as np

attendance = np.array([
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
])

# 1. Total attendance per student (row sum)
student_total = np.sum(attendance, axis=1)

# 2. Attendance on Day 4 (column 3)
day4 = attendance[:, 3]

# 3. Overall percentage
overall_percentage = (np.mean(attendance)) * 100

print("Student total: ",student_total)
print("Day 4: ",day4)
print("Overall percentage: ",overall_percentage)