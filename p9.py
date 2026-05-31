# Quadratic Equation
# ax2+bx+c=0

# where a,b and c are real numbers and a!=0

# ( -b +- (b2 - 4ac)1/2)/(2a)

import math

# input coefficients
a=float(input("Enter the coefficient a: "))
b=float(input("Enter the coefficient b: "))
c=float(input("Enter the coefficient c: "))

# Calculate The discriminant
dis = b**2 - 4*a*c

if dis > 0 :
    root1 = (-b + math.sqrt(dis)) / (2*a)
    root2 = (-b + math.sqrt(dis)) / (2*a)

    print(f"Root 1 : {root1}")
    print(f"Root 2 : {root2}")
    
elif dis == 0:
    root =-b / (2*a)
    print(f"Root: {root}")

else:
    # Complex roots for negative
    real_part =-b / (2*a)
    imaginary_part = math.sqrt(abs(dis)) / (2*a)

    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")