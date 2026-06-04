# Printing the fibonacci sequence
num = int(input("Enter how many terms you want: "))

n1, n2 = 0, 1
count = 0

print("Fibonacci Sequence:")

# If the user asks for 0 or negative terms
if num <= 0:
    print("Please enter a positive integer.")
else:
    while count < num:
        print(n1)        # 1. Print the current number
        
        nth = n1 + n2    # 2. Calculate the next number
        
        # 3. Swap the values (Shift them forward)
        n1 = n2          
        n2 = nth         
        
        count += 1       # 4. Increment loop counter