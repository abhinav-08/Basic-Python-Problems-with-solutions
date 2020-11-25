from collections import Counter
dictonary1 = {'a': 100, 'b': 200, 'c':300}
dictonary2 = {'a': 300, 'b': 200, 'd':400}
res = Counter(dictonary1) + Counter(dictonary2)

print(res,Counter(dictonary1))