string = input("Please enter the string \n")
if len(string)>=3:
    if string[-3:]=="ing":
        string += 'ly'
    else:
        string +="ing"
print(string)
