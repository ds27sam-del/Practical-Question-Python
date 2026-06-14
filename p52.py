# Find the larges value from list
l1=[10,20,30,50,80,40,100]
mini=l1[0]
for i in l1:
    if i > mini:
        mini=i
print(f"The largest value is : {mini}")