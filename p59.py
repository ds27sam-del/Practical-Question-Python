# Program to Count occurrences of an element in a list
def main():
    l1=[1,2,3,4,5,6,2,5,4,6,2,1,4,5,2,3,6,5,8,5,4,2,2,5]
    n=int(input("Enter the number you want to count : "))
    seen=count_oc(l1,n)

    print(f"The value {n} appears {seen} times in the list .")

def count_oc(l1,n):
    count=l1.count(n)
    return count

if __name__=="__main__":
    main()