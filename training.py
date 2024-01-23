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