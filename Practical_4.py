a = int(input("Enter the Number : "))

b = set()

while a > 0 : 
    temp = a % 10
    a = a//10
    b.add(temp)

print("Result : " , b)    

