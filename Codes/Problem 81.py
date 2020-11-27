fruit = ['Apple', 'Oranges', 'Peach', 'Kiwi', 'Lemon', 'Mango']
with open('abc.txt', "w") as myfile:
        for f in fruit:
                myfile.write("%s\n" % f)

content = open('abc.txt')
print(content.read())