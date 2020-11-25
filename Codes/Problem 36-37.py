string = input("Please enter the string \n").split(" ")
startIndex = -1
endIndex = -1
flag = -1
result = ''
for i in range(len(string)) :
    if string[i] == 'not':
        startIndex = i
    if string[i] == 'poor':
        endIndex = i
print(startIndex,endIndex,len(string))
if startIndex<endIndex:
    for i in range(len(string)):
        while i>=startIndex and i <= endIndex:
            print(i)
            i += 1
            flag = 1
            print(result)
        if flag == 1:
            result += ' good'
        print(result)
        result += " "+string[i]


print("result is ", result)