filename = open('abc.txt','r')
print(filename.closed)
filename.close()
print(filename.closed)