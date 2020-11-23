string = input("Please Enter the String \n\n")
uppercase = int(0)
lowercase = int(0)
specialchars = int(0)
for i in string:
    if ord(i)<=122 and ord(i)>=97:
        lowercase += 1
    elif ord(i)<=90 and ord(i)>=65:
        uppercase += 1
    else:
        specialchars +=1

print("Lowercase - ",lowercase,"\nUppercase - ", uppercase,"\nSpecial characters - ", specialchars)

