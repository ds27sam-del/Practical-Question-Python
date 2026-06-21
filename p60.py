# Program to find words which are greater than given length k

def main():
    word_l=["apple", "banana", "cherry", "date", "elderberry", "dragon fruit"]
    k=int(input("Enter the word length : "))
    word_len=se_word(word_l,k)
    print(f"Word longer then {k} characters : {word_len}")
    
def se_word(word_l,k):
    result=[]
    for i in word_l:
        if len(i) > k:
            result.append(i)
    return result

if __name__=="__main__":
    main()