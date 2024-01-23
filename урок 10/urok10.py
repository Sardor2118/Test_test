class Parents:
    def __init__(self):
        pass

class Moderator(Parents):
    def __init__(self):
        pass


class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

class SuperCar(Car):
    def __init__(self, model, color, year, sponsor):
        super().__init__(model, color, year)
        self.sponsor = sponsor

#множество наслдеввание
class Parent1:
    pass
class Parent2:
    pass
class Child(Parent1, Parent2):
    pass

class Car:
    @classmethod
    def ehat(self):
        print('Edet')

nexia = Car
nexia.ehat()

data_base = {}
class Worker:
    def __init__(self, name, work):
        self.name = name
        self.work = work
        # Сохраняем данные в базе данных
        data_base[self.name] = self.work
class Manager(Worker):
    def __init__(self, name, work):
        super().__init__(name, work)
        # Сохраняем данные в базе данных
        data_base[self.name] = self.work
    def check_workers(self, password):
        password_check = 123
        # проверяем правильно ли введен пароль
        if int(password) == password_check:
            return data_base
        else:
            return "Неправильный пароль"

while True:
    menu = input("Кем вы являетесь?")
    if menu.lower() == "работник":
        worker = Worker(input("Введите своё имя:"), input("Введите должность: "))
    if menu.lower() == "менеджер":
        manager = Manager(input("Введите своё имя:"), input("Введите должность: "))
        password = input("Введите пароль для показа базы данных:")
        print(manager.check_workers(password))