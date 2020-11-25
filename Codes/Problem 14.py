string = input("Please enter the string \n").split(' ')
frequency = {}
for i in string:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
for i in frequency:
    print("frequency of '", i, "' is ", frequency[i])