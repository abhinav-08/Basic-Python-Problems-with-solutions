string = input("Please enter the string")
result=string[0]
for i in range(1,len(string)):
    if(string[i]==string[0]):
        result=result+'$'
    else:
        result = result + string[i]
print(result)