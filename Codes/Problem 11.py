string = input("Please enter the string \n")
if len(string)<2:
    print("Empty string")
else:
    print(string[0]+string[1]+string[-2]+string[-1])