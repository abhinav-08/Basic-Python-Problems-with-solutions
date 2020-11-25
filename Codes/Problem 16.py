list = (input("Please enter the elements of list seprated with a space \n")).split(" ")
result = []
for i in list:
    if i in result:
        pass
    else:
        result.append(i)
print(result)