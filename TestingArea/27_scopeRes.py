from math import e
a = 3


def func1():
    def func2():
        a = 1
        print(f"{a} is Local")
    func2()
    a = 2
    print(f"{a} is Enclosed")


func1()
print(f"{a} is Global")
print(f"{e} is Built In")

# LEGB is the order
