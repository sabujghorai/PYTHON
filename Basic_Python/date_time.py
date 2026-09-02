from datetime import date
from datetime import datetime
d = date(1926,8,19) # sould be in year,Month and date
print(d)


# Getting today's date
today = date.today()
print(today)
print(today.year) # Prints the present year
print(today.month) # prints the present month
print(today.day) # prints the present day


# printing the todays date and time
dt = datetime(2006, 9, 6, 16, 50, 40)  # datetime(year, month, day, hour, minute, second)
print(dt)


# Printing the today's actual current date and time 
now = datetime.now()
print(now)