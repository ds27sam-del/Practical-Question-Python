# Find the cube sum of first n natural numbers ?

def main():
    n=int(input("Enter the positive value of n : "))
    
    if n<=0 :
        print("Please Enter a positive value :")
    else :
        total=sum([i**3 for i in range(1,n+1)])
            
    print(f"The cube sum of first {n} natural numbers is : {total}")

if __name__=="__main__":
    main()