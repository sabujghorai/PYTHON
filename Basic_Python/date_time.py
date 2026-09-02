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

formatted = now.strftime("%d-%m-%y") # The strftime is changes the format i want
day = now.strftime("%d")  # The strftime %d shows the day 
month = now.strftime("%m")  # The strftime %m shows the month 
year = now.strftime("%y")  # The strftime %y shows the year

print(formatted)
print(day)
print(month)
print(year)