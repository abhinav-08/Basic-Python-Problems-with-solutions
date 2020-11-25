string = input("Please enter the string \n")
dictonary = {}

for i in string:
    if i in dictonary:
        dictonary[i] +=1
    else:
        dictonary[i] = 1
print(dictonary)