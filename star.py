a = int(input("Enter the length of series : "))

print("In Single Column")
for i in range(0, a):
    {print("*")}

print("In Triangle Form ")

for i in range(0, a + 1):
    {print(i * "*")}

print("In Reverse Traingle Form ")

for i in range(1, a + 1):
    {print((a - i) * " ", end=(i * "*")), print("")}

print("In Pyramid Form ")
for i in range(1, a + 1):
    {print((a - i) * " ", end=(((2 * i) - 1) * "*")), print("")}

for i in range(a - 1, 0, -1):
    {print((a - i) * " ", end=((2 * i) - 1) * "*"), print("")}
