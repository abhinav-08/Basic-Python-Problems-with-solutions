dictonary = {
    "value1":2,
    "value2":4,
    "value3":1,
    "value4":7,
}

max = -1
min = 1000
for i in dictonary:
    if dictonary[i]>max:
        max = dictonary[i]
    elif dictonary[i]<min:
        min = dictonary[i]
print("Maximum value is - ", max, "Minimum value is - ",min)