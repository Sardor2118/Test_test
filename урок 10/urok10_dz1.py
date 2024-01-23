class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Gav!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

dog = Dog()
cat = Cat()
cow = Cow()

dog.make_sound()
cat.make_sound()
cow.make_sound()