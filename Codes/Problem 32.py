from datetime import date, timedelta

for i in range(0,6) :
	date = date.today() + timedelta(i)
	print(date)