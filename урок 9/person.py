class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person('Sardor', 22)
person2 = Person('Azza', 23)

print(f'Ваше имя: {person1.name}, а ваш возраст: {person1.age}')
print(f'Ваше имя: {person2.name}, а ваш возраст: {person2.age}')
