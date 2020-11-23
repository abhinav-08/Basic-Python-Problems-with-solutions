def nearthousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))


value = int(input("Please Enter the value\n\n"))
print(nearthousand(value))