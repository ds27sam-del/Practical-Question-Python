# Remove empty list from the list
l1=[[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
filter_l1=[i for i in l1 if i ]
print(f"List after removing the empty list : \n{filter_l1}")