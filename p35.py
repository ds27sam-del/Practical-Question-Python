l1=[10,20,30,40,50]

k=int(input("Enter the value for array split : "))

if k<= 0 or k>= len(l1):
    print("0")
else:
    end=l1[k:]
    start=l1[:k]
    result=end+start
    print(f"The list is : \n {result}")
