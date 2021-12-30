def isnumerical(l1):
    print()
    if l1[1].isdigit() == True:
        count = 0
        for i in range(0, n):
            c = int(l1[i])
            if c % 2 != 0:
                count += 1
        print("This is list of numbers.")
        print("The number of odd values is", count)
    else:
        str1 = ""
        for i in range(0, len(l1)):
            a = l1[i]
            if len(a) > len(str1):
                str1 = a
        print("This is list of Strings.")
        print("The largest string is", str1)


def reverse(l1):
    print()
    print("**********REVERSE************")
    print("LIST IS :-", l1)
    l2 = l1[::-1]
    print("REVERSE LIST IS :-", l2)


def search(l1):
    print()
    print("**********SEARCHING************")
    print("LIST IS :-", l1)
    a = input("Enter element for search :- ")
    for i in range(0, len(l1)):
        if l1[i] == a:
            print("Element found at position", i + 1)
            return
    print("Element not found !!!")


def removed(l1):
    print()
    print("**********REMOVING************")
    print("LIST IS :-", l1)
    a = input("Enter element for remove :- ")
    for i in l1:
        if a == i:
            l1.remove(i)
    print("AFTER REMOVE, LIST IS :-", l1)


def sorting():
    print()
    print("**********SORTING************")
    l4 = []
    m = int(input("Enter the number of element in list :- "))

    for i in range(0, m):
        b = int(input("Enter the element of list :- "))
        l4.append(b)
    print()
    print("LIST IS :-", l4)
    l5 = []
    for i in range(0, len(l4)):
        max = 0
        for j in range(0, len(l4)):
            if l4[j] > max:
                max = l4[j]
        l5.append(max)
        l4.remove(max)
    print("AFTER SORTING, LIST IS :-", l5)


def commonMem(l1):
    print()
    print("**********COMMON MEMBER************")
    l2 = []
    m = int(input("Enter the number of element in list 1 :- "))

    for i in range(0, m):
        b = input("Enter the element of list 1 :- ")
        l2.append(b)
    print("List 1 is :- ", l2)

    l3 = []
    n = int(input("Enter the number of element in list 2 :- "))

    for i in range(0, n):
        c = input("Enter the element of list 2 :- ")
        l3.append(c)
    print("List 2 is :- ", l3)

    com = []
    for i in range(0, len(l2)):
        for j in range(0, len(l3)):
            if l2[i] == l3[j]:
                com.append(l2[i])
    print("Common menmber of list 1 and list 2 is :- ", com)


l1 = []
n = int(input("Enter the number of element in list :- "))

for i in range(0, n):
    a = input("Enter the element of list :- ")
    l1.append(a)

isnumerical(l1)
reverse(l1)
search(l1)
removed(l1)
sorting()
commonMem(l1)
