# swap the two variables using the temp variable

a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))

print(f"The original values : a:{a}, b:{b}")

temp=a
a=b
b=a

print(f"The result after swap \n a={a} \n b={b}")