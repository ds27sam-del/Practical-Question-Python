# BMI Calculator

def main():
    print("Well come to BMI calculator ")
    kg=float(input("Enter your weight : "))
    m=float(input("Enter your height : "))
    result=round((kg/(m*m)),2)
    if result <=18.5:
        print("You are under weight")
    elif 18.5 < result and result >=24.5:
        print("Yor weight is normal ")
    elif 24.5 < result and result >= 29.29:
        print("You are over weight")
    else:
        print("You are obese ") 

    print(f"the result is : {result}")

if __name__=="__main__":
    main()