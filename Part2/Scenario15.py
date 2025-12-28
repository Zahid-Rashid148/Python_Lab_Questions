import numpy as np

marks = np.array([
    [80, 75, 90],
    [70, 85, 88],
    [92, 78, 84],
    [65, 80, 70]
])

# 1. Average per student
student_avg = np.mean(marks, axis=1)

# 2. Subject 2 marks
subject2 = marks[:, 1]

# 3. Class average
class_avg = np.mean(marks)

print("Student averages:", student_avg)
print("Subject 2 marks:", subject2)
print("Class average:", class_avg)
