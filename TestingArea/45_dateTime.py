import datetime

date = datetime.date(2035, 1, 1)
today = datetime.date.today()
time = datetime.time(12, 30, 40)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%Y")
target_datetime = datetime.datetime(2020, 1, 1, 12, 30,00)
current_datetime = datetime.datetime.now()

print(date)
print(today)
print(time)
print(now)

if target_datetime < current_datetime:
    print("Target Date has already passed!")
else:
    print("Target Data has not yet passed!")
