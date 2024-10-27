import time

my_time = int(input("Enter time as Seconds: "))

for i in range(my_time, 0, -1):
    hours = (i // 3600)
    minutes = (i // 60) % 60
    seconds = i % 60

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
