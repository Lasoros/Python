from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)

print("days", duration.days)
print("secs", duration.seconds)
print("total_secs", duration.total_seconds())

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1500) #adding a timedelta obj to datetime obj
print(dt1)