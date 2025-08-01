#Date and Time

from datetime import datetime

date_and_time =datetime.now()
print (date_and_time)

year = date_and_time.year
month = date_and_time.month
day = date_and_time.day


hour = date_and_time.hour
minute = date_and_time.minute
second = date_and_time.second
microsecond = date_and_time.microsecond

print(f"The current date and time is {year}/{month}/{day} {hour}:{minute}:{second}")

#We can also create a date and time object by passing a string
date_and_time =datetime.strptime("2025-01-01 12:00:00","%Y-%m-%d %H:%M:%S")