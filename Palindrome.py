def check(word):
    if(word == word[::-1]):
        return True
    return False

word = input("Enter the Word you want to Check : ")

if(check == True):
    print("The given word is a Palindrome.")
else:
    print("The given word is not a Palindrome.")    