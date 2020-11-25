tupleItems = list(input("Please enter the items of tuple seprated eith a comma(',') \n").split(","))
list = []
for i in tupleItems:
    if i in list:
        print(i+" ")
    else:
        list.append(i)


