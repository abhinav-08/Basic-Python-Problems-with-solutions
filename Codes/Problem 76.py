def read_file_first_n(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)


read_file_first_n('testDocument.txt', 2)