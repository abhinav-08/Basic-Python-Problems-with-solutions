file1 = open("testDocument.txt","r")
file2 = open("output.txt","w")
line = file1.readline()
while line:
    file2.write(line)
    line = file1.readline()
file1.close()
file2.close()