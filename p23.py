# Find HCF from 2 numbers

import math

num1=int(input("Enter the smaller value :"))
num2=int(input("Enter the higher value: "))


if( num1 == 0 or num2 ==0 ):
    print("The result is : 0")
else:
    print(f"The H.C.F of {num1} and {num2} is : {math.gcd(num1,num2)}")