class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("WOOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOOW!")


class Car:

    alive = False

    def speak(self):
        print("HOONK!")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    if animal.alive:
        print("It's alive!")
    else:
        print("It's dead...")
