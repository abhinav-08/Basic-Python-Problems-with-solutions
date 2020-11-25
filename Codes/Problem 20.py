dictonary = {
    "value1":2,
    "value2":4,
    "value3":1,
    "value4":7,
    "value5":4,
    "value6":8,
    "value7":7,
}

list = []
for i in dictonary:
    if dictonary[i] in list:
        pass
    else:
        list.append(dictonary[i])
print(list)