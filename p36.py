def main():
    ar1=[1,2,2,3]
    ar2=[3,2,1]
    ar3=[1,3,2,4]

    print(f"arr1 is monotonic : {mono(ar1)}")
    print(f"arr2 is monotonic : {mono(ar2)}")
    print(f"arr3 is monotonic : {mono(ar3)}")

def mono(ar):
    increasing = decreasing = True

    for i in range(1,len(ar)):
        if ar[i] > ar[i-1]:    
            decreasing = False
        elif ar[i] < ar[i-1]:
            increasing = False
        
    return increasing or decreasing

if __name__=="__main__":
    main()