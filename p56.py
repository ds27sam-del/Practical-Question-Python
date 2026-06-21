# Odd numbers in the list print them
l1=[]
for i in range(1,11):
    l1.append(i)
odd_no=[num for num in l1 if num % 2 != 0]
print(f"Odd numbers in the list :\n{l1} \nresult is \n{odd_no}")