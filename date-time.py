# dates
from datetime import datetime
now = datetime.now()
print(now)
month = now.month
day = now.day
year = now.year
print(f"Today is {month} {day}, {year}")

current_hour = now.hour
current_minutes = now.minute
current_seconds = now.second

print(f"The time is {current_hour} hour {current_minutes} minutes and {current_seconds} seconds")

# difference between two point in time
from datetime import date, timedelta
today = date(year= 2026, month=1,day=10)
christmas = date(year=2026, month=12, day=25)
time_left = christmas - today
print(time_left)

t1 = timedelta(weeks=2, days=10, hours=20, seconds=45)
t2 = timedelta( hours = 12, minutes = 00, seconds=30)
t3 = t2 - t1
print(time_left, t3)
