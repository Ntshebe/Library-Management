"""Task 2: Comprehensions (lists and sets).
The libraries is using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:
§ Create a normal and comprehensive list that will display the codes.
§ Create a normal and comprehensive list that will add the codes together for auditing purpose.
§ Create a normal and comprehensive list that will display only codes that are tracked by odd 
numbers.
§ Create a set to display the list of codes"""

number = [14, 15, 16, 17, 18, 19, 20]

#Create a normal list that will display the codes.
norDis= []
for n in number :
 norDis.append(n)

print("Normal list ",norDis)

#Create a comprehensive list that will display the codes. 

comDis = [n for n in number]

print("comprehensive List", comDis)

#Create a normal list that will add the codes together for auditing purpose.

Add = []
sumN=0
for m in number:
 sumN= sumN + m

Add.append(m)
print("norma list added", sumN)

#Create acomprehensive list that will add the codes together for auditing purpose.

sumCo= 0
AddCo =[sumCo:= sumCo +mCo for mCo in number]
print("added Compehensive list ", AddCo)

#Create a normal list that will display only codes that are tracked by odd numbers

oddN = []

for c in number:
 if c%2 !=0:
   oddN.append(c)

print("odd number in nomal list", oddN)

#Create a comprehensive list that will display only codes that are tracked by odd numbers

oddC = [ co for co in number if co%2!=0]

print("odd number in a Comprehensive list",oddC)

#Create a set to display the list of codes
setList = set(number)

print("Display set List : ", setList)