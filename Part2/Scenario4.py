import numpy as np

marks = np.array([
    [78, 85, 90],
    [88, 92, 79],
    [60, 75, 70],
    [95, 89, 96]
])

# 1. Average marks per student (row-wise)
avg_marks = np.mean(marks, axis=1)

# 2. Marks of Subject 1 (column index 0)
subject1 = marks[:, 0]

# 3. Add 5 grace marks to Subject 3 (column index 2)
marks[:, 2] += 5

print("Average marks: ",avg_marks)
print("Subject 1: ",subject1)
print("Updated marks: ",marks)