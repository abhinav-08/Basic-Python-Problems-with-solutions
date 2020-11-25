def commonElementChecker(list1, list2):
    flag = '-1'
    for i in list1:
        if i in list2:
            flag = '1'
            break
    if flag == '1':
        return "Yes list1 and list2 have atleast 1 common member"
    else:
        return "No list1 and list2 don't have any common member"


list1 = (input("Please enter the elements of first list  seprated with a space \n")).split(" ")
list2 = (input("Please enter the elements of second list seprated with a space \n")).split(" ")

print(commonElementChecker(list1, list2))