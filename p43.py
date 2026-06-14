# Check the given nuber is Disarium number

def  Dis_logic(num):
    num_str=str(num)
    dig_num=sum(int(i) ** (index +1) for index, i in enumerate(num_str))

    return dig_num == num

def main():
    num = int(input("Enter a number : "))

    if Dis_logic(num):
        print(f"The {num} is an Disarium number.")
    else:
        print(f"THe {num} is not an Disarium number. ")

if __name__=="__main__":
    main()