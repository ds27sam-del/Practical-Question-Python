# Print all Prime numbers from n to m interval
n = int(input("Enter the Start value: "))
m = int(input("Enter the End value: "))

print(f"Prime numbers between {n} and {m} are:")

# Loop through every number in the range
for num in range(n, m + 1):
    # Primes must be greater than 1
    if num > 1:
        # Check for factors from 2 up to num - 1
        for i in range(2, num):
            if (num % i) == 0:
                break  # Found a factor! Not prime, so stop checking this 'num'
        else:
            # This else belongs to the FOR loop, NOT the IF statement.
            # It only runs if the loop finished without hitting 'break'.
            print(num, end=" ")

print()  # Just prints a final newline