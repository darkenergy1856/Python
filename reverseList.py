list = [1,2,3,4,5,6,7,8,9,10]
listTemp = []
list.reverse()

size = len(list)

for x  in range(0 , size) : 
    listTemp.append(list[size - 1 - x])

print("Original : " , list)
print("Reverse Function : " , list)
print("Updated Function : " , listTemp)