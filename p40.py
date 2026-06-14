# Write a program to sort Words in alphabetic order
my_str=input("Enter the names / strings : ")

words =[word.capitalize() for word in my_str.split()]

words.sort()

print("The sorted words are : ")

for word in words:
    print(word)