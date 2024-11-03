try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You cant divide by zero!")
except ValueError:
    print("Enter only numbers please!")
finally:
    print("Do some shit!")
