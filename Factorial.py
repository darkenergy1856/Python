a = int(input("Enter the value : "))
result = 1

if (a == 0):
    print("Result : ", 1)
    exit(0)

for i in range(1, a + 1):
    result = result * i

print("Result : ", result)

result = 1

for i in range(a, 1, -1):
    result = result * i

print("Result : ", result)

result = 1

temp = a

while (temp > 1):
    result = result * temp
    temp = temp - 1

print("Result : ", result)

temp = 1
result = 1

while (temp <= a):
    result = result * temp
    temp = temp + 1

print("Result : ", result)
