a = int (input ("First Side : "))
b = int (input ("Second Side : "))
c = int (input ("Third Side : "))


def areaPermimeter(a , b , c) :
    if(a+b>c)and(b+c>a)and(a+c>b) :
        semPer = (a+b+c)*0.5
        area=((semPer*(semPer-a)*(semPer-b)*(semPer-c))**0.5)
        print("Area of Triangle is  : " , area)
        print("Perimeter of Triangle is : " , semPer*2)
        return(area , semPer*2)
    else :
        print("Given sides dosn't satisfy the criteria of Triangle.")

print(areaPermimeter(a,b,c))    

