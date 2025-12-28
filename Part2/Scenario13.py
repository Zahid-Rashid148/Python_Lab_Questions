import numpy as np

angles = np.array([
    [10, 12, 14, 16, 18, 20],
    [20, 22, 24, 26, 28, 30],
    [30, 32, 34, 36, 38, 40]
])

# 1. Extract angles at time step 4
time_step_4 = angles[:, 3]

# 2. Average angle of each joint
avg_angles = np.mean(angles, axis=1)

# 3. First 5 time steps of joint 2
joint2_first5 = angles[1, :5]

print("Time step 4:", time_step_4)
print("Average angles:", avg_angles)
print("Joint 2 first 5 steps:", joint2_first5)
