list = (input("Please enter the list elements seprated by a space comma(',')")).split(",")
sum = 0
for i in list:
    sum += int(i)
print(sum)