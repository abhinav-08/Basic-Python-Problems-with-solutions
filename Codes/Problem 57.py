string = input("Please enter the string \n")
digit = 0
alphabet = 0

for i in string:
    if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
        alphabet +=1
    elif (ord(i)>=48 and ord(i)<=57):
        digit +=1
    else:
        pass
print("Digits - ", digit," Alphabets - ", alphabet)