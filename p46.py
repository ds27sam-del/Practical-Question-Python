# Program to check the happy numbers between 1 to 100
def ha_no(num):
    seen=set()
    while num != 1 and num not in seen:
        seen.add(num)
        num=sum(int(i) ** 2 for i in str(num))
    return num==1
def main():
    ha_num=[]
    for num in range(1,101):
        if ha_no(num):
            ha_num.append(num)
    print(f"The happy numbers between 1 and 100 : \n {ha_num}")

if __name__=="__main__":
    main()