class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print("Gonna go now!")


class Predator(Animal):
    def hunt(self):
        print("Why are you running!?")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Stew")
hawk = Hawk("Americ")
fish = Fish("Blue")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

rabbit.sleep()
hawk.eat()
fish.eat()
