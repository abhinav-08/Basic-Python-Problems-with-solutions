string = input("Please enter the string \n").split(",")
unique = []
for i in string:
    if i in unique:
        pass
    else:
        unique.append(i)
unique.sort()
print(unique)