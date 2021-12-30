a = int(input("Enter first side : "))
b = int(input("Enter second side : "))
c = int(input("Enter third side : "))
s = (a+b+c)/2
if (a == b == c):
    print("Equilateral Triangle having perimeter ", 3*a)
elif (a == b or b == c or a == c):
    print("Isosceles Triangle having area ", ((s*(s-a)(s-b)(s-c))**0.5))
else:
    print("Scalene Triangle having area ", ((s*(s-a)(s-b)(s-c))**0.5))