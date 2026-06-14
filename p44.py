# Program to print all numbers between 1 to 100
def  Dis_logic(num):
    num_str=str(num)
    dig_num=sum(int(i) ** (index +1) for index, i in enumerate(num_str))
    return num==dig_num
dis_nums=[num for num in range(1,101) if Dis_logic(num)]
print("disarium numbers between 1 to 100 is :")
for num in dis_nums:
    print(num,end="|")