Python Code
# SESSION 10 – Edge Detection (Gradient Magnitude)

import math

# Step 1: Input gradient values
Gx = 5
Gy = 12

# Step 2: Compute edge strength
edge = math.sqrt(Gx**2 + Gy**2)

# Step 3: Display result
print("Edge Strength =", int(edge))

print("\nProgram Executed Successfully")
