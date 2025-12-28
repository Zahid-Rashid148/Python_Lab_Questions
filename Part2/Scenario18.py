import numpy as np

image = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

# 1. Top-left 2×2 block
block = image[:2, :2]

# 2. Increase brightness by +50
bright_image = image + 50

# 3. Flatten image
flat_image = image.flatten()

print("2x2 Block:", block)
print("Brightened Image:", bright_image)
print("Flattened Image:", flat_image)
