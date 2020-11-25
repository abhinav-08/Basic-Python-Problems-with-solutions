listAsString = (input("Please enter the elements of list seprated with a space \n")).split(" ")
sum = 0
for i in listAsString:
    sum += int(i)
print(sum)
