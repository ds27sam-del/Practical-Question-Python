# Even numbers in the list print them
l1=[]
for i in range(1,11):
    l1.append(i)
even_no=[num for num in l1 if num % 2 == 0]
print(f"Even numbers in the list :\n{l1} \nresult is \n{even_no}")