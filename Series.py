def Factorial(temp) : 
    result = 1
    for i in range(temp, 1, -1):
        result = result * i
    return(result)   

a = int (input("Enter the value : "))

finalResult = 0.000

for i in range (1 , a+1) : 
    finalResult = finalResult + (i/Factorial(i))

print("Result : " , finalResult) 