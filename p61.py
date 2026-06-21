# Program to remove n character from a string.
def re_move(word, c):
        new_word = word.replace(c, "")
        return new_word

def main():
    word = input("Enter words : ")
    c = input("Enter the character you want to remove : ")
    result = re_move(word, c)
    print(f"Result is: {result}")

if __name__ == "__main__":
    main()