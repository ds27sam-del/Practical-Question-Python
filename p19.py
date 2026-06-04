num=int(input("Enter the number: "))
n_str=str(num)
n_digit=len(n_str)
sum_of_powers=0
temp_n=num
while temp_n>0:
    digit =temp_n % 10
    sum_of_powers += digit ** n_digit
    temp_n //=10
if sum_of_powers == num:
    print(f"{num} is an Armstrong number .")
else :
    print(f"{num} is not an Armstrong number")