# Rotate the array

l1 = [10, 20, 30, 40, 50, 60]
r = 40

# 1. Effective rotations nikalo
n = len(l1)
r = r % n  # 10 % 6 = 4

# 2. Slicing se inplace update karo
l1[:] = l1[r:] + l1[:r]

print(f"Result is : {l1}")
# Output: [50, 60, 10, 20, 30, 40]