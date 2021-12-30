def sum(a,b):
    return a+b

def multiplication(a,b):
    return a*b

def subtraction(a,b):
    return a-b

def division(a,b):
    return a/b   

a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))

print ("1. Sum" ,"2. Subtraction","3. Multiplication" , "4. Division" )

c=int(input("Enter your Choice  : "))

if (c==1):
    print("Result is : ",sum(a,b))
elif(c==2):
    print("Result is : ",subtraction(a,b))
elif(c==3):
    print("Result is : ",multiplication(a,b))        
elif(c==4):
    print("Result is : ",division(a,b))
