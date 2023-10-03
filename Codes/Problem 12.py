
def modify_input(input_string):
    temp = input_string[0]
    input_string = input_string.replace(temp, '$')
    return temp+input_string[1:]


user_input_string = input("Enter String - ")
print(modify_input(user_input_string))
result=string[0]
for i in range(1,len(string)):
    if(string[i]==string[0]):
        result=result+'$'
    else:
        result = result + string[i]
print(result)
