def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid Day"


print(day_of_week(7))


def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case _:
            return False


print(is_weekend("Saturday"))

