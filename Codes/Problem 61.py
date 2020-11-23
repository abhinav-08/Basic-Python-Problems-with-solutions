string = input("--Please enter the string-- \n").split('-')
string.sort()
result = ''
for word in string:
    result += word+'-'
print(result)