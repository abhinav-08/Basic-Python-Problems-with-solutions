def duplicateremoval(userlist):
    result=[]
    for i in userlist:
        if i in result:
            pass
        else:
            result.append(i)
    return result


l = input("Please Enter the elements of array seprated with space \n").split(" ")
print(duplicateremoval(l))