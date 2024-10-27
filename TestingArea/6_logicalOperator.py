temp = 20
is_raining = False
is_sunny = True

if temp > 30 or temp < 5 and is_raining:
    print("The outdoor event is cancelled!")
else:
    print("WE PARTY!!!")

if temp >= 30 and is_sunny:
    print("It is Hot and Sunny")
elif temp <= 0 and is_sunny:
    print("It is cold and Sunny")
elif temp <= 0 and not is_sunny:
    print("If is cold and cloudy")
elif 25 > temp > 10 and not is_raining and is_sunny:
    print("Its perfect!")
