# Write a function that finds the sum of the n terms of the following series.
# 1–x2/2!+x4/4!–x6/6!+…xn/n!

import math

constTerm = int(input("Enter the Value of the Constant term : "))
noOfTerms = int(input("Enter the Value for No. of Terms : "))

sum = 0.0

temp = 0

if (noOfTerms == 1):
    print("Result is : ", 1)
    exit(0)

for i in range(noOfTerms):
    if (i % 2 == 0):
        sum = sum + (temp * constTerm / math.factorial(temp))
    else:
        sum = sum - (temp * constTerm / math.factorial(temp))
    temp = temp + 2

print ("Result is : " , sum)
