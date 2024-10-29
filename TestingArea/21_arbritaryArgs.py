# *args - tuple
def add_num(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(add_num(1, 1, 2, 3))


# **kwargs - dict
def print_address(**address):
    for key, value in address.items():
        print(f"{key} - {value}")


print_address(street="123 Fake St", city="Tacloban", province="Leyte", zip="6510")


def fibo(num: int):
    fibo_lisf = [0, 1]
    for i in range(num):
        fibo_lisf.append(fibo_lisf[i] + fibo_lisf[i + 1])
    return fibo_lisf


print(fibo(10))
