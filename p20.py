# Find the Armstrong Number in between 2 values 
l=int(input("Enter the lower value: "))
h=int(input("Enter the highest value: "))

for num in range(l,h+1):
    order=len(str(num))
    temp_num=num
    sum=0
    while temp_num>0:
        digit=temp_num %10
        sum+= digit ** order
        temp_num //= 10
    
    if num==sum:
        print(sum)