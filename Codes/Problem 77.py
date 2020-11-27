def file_read_store_list(fname):
    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        content_list = f.readlines()
        print(content_list)


file_read_store_list('testDocument.txt')