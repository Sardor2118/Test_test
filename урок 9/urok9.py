class User:
    name = 'Jordan'

# ООП (объекто-ориентированное программирование)
# Класс - шаблон
# Объект - заполненный шаблон
# Метод - функция класса
# Аттрибут - характеристика

class Ai:
    sync = 'gpt'

class Human:
    def __init__(self, name, weight, color, age=0):
        self.name = name
        self.weight = weight
        self.color = color
        self.age = age
human1 = Human('AA', 23, 134)

class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes
post = Comment('username', 'text')

class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def stop(self):
        print(f'{self.model} остановилась')

gentra = Car(model = input(), color = input(), year = input())
gentra.stop()

#    def stop(self):
#        print(f'{self.model} остановилась')

#    def change_color(self, new_color):
#        self.color = new_color

#gentra = Car(model = input(), color = input(), year = input())
#gentra.change_color('White')
#gentra.stop()

class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def cash(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
           print("Недостаточно средств")

    def my_balance(self):
        print(self.balance)

bank_user = BankAccount(name = input('Введите имя: '))
while True:
    menu = input('Выберите пункт меню: \n'
                 '1- Ваш баланс \n'
                 '2- Пополнить баланс \n'
                 '3- Снять деньги ')
    if menu == '1':
        bank_user.my_balance()
    elif menu == '2':
        amount = input('Введите деньги: ')
        bank_user.deposit(int(amount))
    elif menu == '3':
        amount = input('Сколько снять денег?: ')
        bank_user.cash(int(amount))
    else:
        print('Нет такой функицц')