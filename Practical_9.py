Marsksheet = {'Mike':[50,60,70,54] , 'Sam':[45,84,70,54] ,'Rohit':[57,42,74,54] , 'Rahul':[29,64,69,54] }

temp = []
marks = 0
sum = 0
name = any

for keys in Marsksheet:
    temp = Marsksheet.get(keys)
    sum = 0 
    for i in temp :
        sum += i
    if sum > marks :
        marks = sum
        name = keys

print ("Student Scoring Highest Marks : " , name)           











