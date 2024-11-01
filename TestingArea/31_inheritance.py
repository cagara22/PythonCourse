class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")


class Dog(Animal):
    def speak(self):
        print("Wooof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


class Mouse(Animal):
    def speak(self):
        print("Squeak!")


dog = Dog("Chock")
cat = Cat("Mr. Sniffles")
mouse = Mouse("Steve")

print(dog.name)
print(cat.name)
print(mouse.name)
dog.eat()
dog.sleep()
dog.speak()