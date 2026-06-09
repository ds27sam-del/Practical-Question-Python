# Find Factorial of number using Recursion.

def main():
    num=int(input("Enter the value:"))
    if num<0:
        print(f"Sorry, Factorial of {num} dose not exist")
    elif num==0:
        print(f"The factorial of {num} is : 0")
    else :
        print(f"The factorial of {num} is : {rec_fact(num)}")

def rec_fact(n):
    if n==1:
        return n
    else:
        return n*rec_fact(n-1)    
    
if __name__== "__main__":
    main()