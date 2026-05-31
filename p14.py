# Checking the number is prime or odd 
num=int(input("Enter the number: "))
Flag =False
if num >1: 
    for i in range(2,num):
        if(num % i)==0:
            Flag=True
            break
if Flag:
    print(f"{num} ,is not a prime number ")
else:
    print(f"{num} , is a prime number")