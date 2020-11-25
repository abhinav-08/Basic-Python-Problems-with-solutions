numbers = input("Please enter the numbers seprated with a comma(',') \n").split(",")
even = 0
odd = 0
for i in numbers:
    if int(i)%2==0:
        even +=1
    else:
        odd +=1
print("Even - ", even," Odd - ", odd)