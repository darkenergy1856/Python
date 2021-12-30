def Area(a, b , c):
    temp=a+b+c/2
    area = ((temp*(temp-a)*(temp-b)*(temp-c))**0.5)    
    return area


c = int(input("Side 1 : "))
d = int(input("Side 2 : "))
e = int(input("Side 3 : "))
print ("Area of the Triangle is : " , Area(c,d,e))

