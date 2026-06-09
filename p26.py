# Make an calculator

while(True):
    c=int(input(f"\tWell come to calculator\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulo\n6.Exit\nEnter your choice : "))
    if c in (1,2,3,4,5,6):
        try:
            a=int(input("Enter the first number : "))
            b=int(input("Enter the second number : "))
        except ValueError:
            print("Invalid input. Please enter a number ")
            continue

        if (c==1):
            print("The result is : ",a+b)
        elif (c==2):
            print("The result is : ",a-b)
        elif (c==3):
            print("The result is : ",a*b)
        elif (c==4):
            print("The result is : ",a/b)
        elif (c==5):
            print("The result is : ",a%b)
        elif (c==6):
            e=input("Do You Want To Exit (y/n) : ")
            if e == 'Y' or 'y':
                print("Visit again . Logout")
                break
            else :
                break
    else:
        print("invalid input")
