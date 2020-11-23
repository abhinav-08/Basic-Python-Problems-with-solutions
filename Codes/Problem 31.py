from datetime import date, timedelta
yest = date.today() - timedelta(1)
tomm = date.today() + timedelta(1)
print('Date Yesterday :',yest)
print('Current Date   :',date.today())
print('Date Tommorrow :',tomm)