tupleList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# for i in range(len(tupleList)):
#     for j in range(i+1,len(tupleList)):
#         print(tupleList[i][1])
def last(n): return n[-1]


def sort_list_last(tuples):
    return sorted(tuples, key=last)


print(sort_list_last(tupleList))

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if tupleList[j][1] > tupleList[j + 1][1]:
#             temp = tupleList[j][1]
#             tupleList[j][1] = tupleList[j + 1][1],
#             tupleList[j + 1][1] = temp