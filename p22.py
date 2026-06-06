# Find lcm from 2 values

import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == 0 or b == 0:
    print("The L.C.M is : 0")
else:
    lcm = abs(a * b) // math.gcd(a, b)
    print(f"The L.C.M is : {lcm}")