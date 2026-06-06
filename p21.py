# Find the sum of Natural Number 

limit =int(input("Enter the limit:"))
sum=0

for i in range(1,limit+1):
    sum+=i
print(f"The Sum of natural numbers up to {limit} is : {sum} ")
