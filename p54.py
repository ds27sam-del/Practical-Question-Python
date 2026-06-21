# Program to find N Largest elements from List

def main():
    l1=[30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]
    n=int(input("Enter the number of top values wanted : "))
    result=Top_l2(l1,n)
    print(f"The {n} largest values in the list are : {result}")

def Top_l2(l1,n):
    s_l1=sorted(l1,reverse=True)
    l2=s_l1[:n]
    return l2

if __name__=="__main__":
    main()