import datetime
x = datetime.datetime.now()

# a) Current date and time
print("Current date is - ", x.strftime("%x"), " and time is - ", x.strftime("%X"))
# b) Current year
print("Current year is - ", x.strftime("%Y"))
# c) Month of year
print("Current Month of year - ", x.strftime("%B"))
# d) Week number of the year
print("Current Week number of the year - ", x.strftime("%W"))
# e) Weekday of the week
print("Current Weekday of the week - ", x.strftime("%A"))
# f) Day of year
print("Current Day of year - ", x.strftime("%j"))
# g) Day of the month
print("Current Day of the month - ", x.strftime("%d"))
# h) Day of week
print("Current Day of week - ", x.strftime("%w"))