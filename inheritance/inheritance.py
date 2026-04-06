class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()  # Some sound


class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()  # Bark

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Buddy", "Labrador")
print(d.name, d.breed)  # Buddy Labrador


class Animal:
    def eat(self):
        print("Eating")

class Pet:
    def play(self):
        print("Playing")

class Dog(Animal, Pet):
    pass

d = Dog()
d.eat()   # Eating
d.play()  # Playing


class Animal:
    def speak(self):
        print("Some sound")

class Mammal(Animal):
    pass

class Dog(Mammal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()  # Bark