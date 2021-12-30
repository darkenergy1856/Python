def Fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def factorial(n):
    temp = 1
    for i in range(2, n + 1):
        temp = temp * i
    return temp


a = int(input("Enter the Value : "))

temp1 = Fibonacci(a)
list = [Fibonacci(a)]

list.append(factorial(temp1))

print("Value after Calculation is : ", list)
