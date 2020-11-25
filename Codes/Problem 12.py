def modify_input(input_string):
    temp = input_string[0]
    input_string = input_string.replace(temp, '$')
    return temp+input_string[1:]


user_input_string = input("Enter String - ")
print(modify_input(user_input_string))
