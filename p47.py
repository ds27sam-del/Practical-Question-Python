# program to check Harshad number.

def hash_no(num):
    dig_sum=sum(int(i) for i in str(num))
    return num % dig_sum == 0

def main():
    num=int(input("Enter a number: "))
    if hash_no(num):
        print(f"{num} is a Harshad Number.")
    else:
        print(f"{num} is nit a Harshad Number.")
if __name__=="__main__":
    main()