#######Datetime module

import datetime

t = datetime.time(hour= 5, minute= 25, second= 1, microsecond= 3)
print(t)

print(t.microsecond)
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)
print(datetime.time.tzinfo)


today = datetime.date.today()
print(today)

print(today.timetuple())
print(today.day)
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)

d1 = datetime.date(2015,3,11)
print(d1)

d2 = d1.replace(year = 1990)
print(d2)

print(d1 - d2) # uses timedelta class



