import datetime
def conversion(string):
    format = '%b %d %Y %I:%M%p'
    datetime_string = datetime.datetime.strptime(string, format)

    return datetime_string


datestring = input("Please enter string as 'Month' 'Date' 'Year' 'HH:MMAM/PM'")
print(conversion(datestring))