# Program to find smallest value from list
l1=[100,20,30,10,50]
mini=l1[0]
for i in l1:
    if i< mini:
        mini=i
print(f"The smallest value from the list\n{l1}\nis : {mini}")