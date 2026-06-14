# Program to check the happy number 
def ha_no(num):
    seen=set()
    while num != 1 and num not in seen:
        num=sum(int(i) ** 2 for i in str(num))
    return num==1
def main():
    num=int(input("Enter a number:"))
    if ha_no(num):
        print(f"{num} This is an happy number .")
    else:
        print(f"{num} is not an happy number.")
if __name__=="__main__":
    main()