# Program to remove Punctuation from string

Pun='''!()-[]{};:'",<>./?@#$%^&*_~'''
str1=input("Enter the string: ")
str2=""
for i in str1:
    if i not in Pun:
        str2=str2+i
print("String after removing punctuation: ",str2)