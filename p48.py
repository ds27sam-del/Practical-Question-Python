# Program to print all pronic numbers between 1 to 100

def pro_no(num):
    for n in range(1,int(num**0.5) +1):
        if n * (n+1) == num:
            return True
    return False

def main():
    print("Pronic numbers between 1 to 100:")
    for i in range(1,101):
        if pro_no(i):
            print(i,end=" | ")
if __name__=="__main__":
    main()