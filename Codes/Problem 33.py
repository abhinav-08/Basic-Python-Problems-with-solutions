from datetime import date, timedelta

d0 = date(2008, 8, 13)
d1 = date(2008, 8, 19)
delta = d1 - d0 - timedelta(1)
print(delta.days)
print(delta.days)