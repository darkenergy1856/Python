str1 = input("Enter a String :-\n")
print("Your entered string is :- ", str1)
choice = 1
while(choice != 6):
    print("----------Menu----------")
    print("1. Length of string ")
    print("2. Return maximum of strings ")
    print("3. Replace vowels by #")
    print("4. Find number of words ")
    print("5. Check palindrome ")
    print("6. Exit ")
    choice = int(input("Enter your choice :- "))
    if(choice == 1):
        print("Lemgth of string 1 is", len(str1))
    elif(choice == 2):
        str2 = input("Enter second String :-\n")
        str3 = input("Enter third String :-\n")
        print("Your entered second string is :- ", str2)
        print("Your entered third string is :- ", str3)
        temp = str1
        if len(str2) > len(str1) : 
            temp = str2
        if len(str3) > len(str2) :
            temp = str3   
        print("Maximum of three strings is :-" , temp)     
    elif(choice == 3):
        for i in str1:
            if(i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U'):
                str1 = str1.replace(i, "#")
        print("Replace vowels by # -:", str1.replace(i, "#"))
    elif(choice == 4):
        str4 = str1.split(" ")
        print("The number of word in string 1 is", len(str4))
    elif(choice == 5):
        a = str(input("Enter a string to check palindrome :-\n"))
        if (a == a[::-1]):
            print("It is palindrome string. ")
        else:
            print("It is not a palindrome string.")
    elif(choice == 6):
        exit()
    else:
        print("Invalid Choice !!!")
