def file_read_show_len(fname):
    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        content_list = f.readlines()
        print(len(content_list))


file_read_show_len('testDocument.txt')