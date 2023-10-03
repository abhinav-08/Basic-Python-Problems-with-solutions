def get_key(tup):
    return tup[1]


def sort_tuple(tuples):
    return sorted(tuples, key=get_key)


tuple_list = list(tuple(map(int, input().split())) for r in range(int(input('enter no of rows : '))))
print(sort_tuple(tuple_list))