list = input("Please provide the elements of list seprated wit comma(',') \n").split(",")
n = input("Please enter the value of n \n")
print(list)
finalList = []
for j in range(1, int(n)+1):
    for i in list:
        finalList.append(str(i)+str(j))
print(finalList)