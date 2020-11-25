list = (input("Please enter the list elements seprated by a comma(',')")).split(",")
res = 1
for i in list:
    res *= int(i)
print(res)