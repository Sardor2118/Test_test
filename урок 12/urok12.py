#  Первая тема if elif else главная логика в коде
first = str(input('Игрок 1 '))
matem = input('Игрок 2 ')

if matem == 'камень' and first == 'ножница':
    print('Игрок 2 победил')
elif matem == 'камень' and first == 'камень':
    print('ничья')
elif matem == 'камень' and first == 'бумага':
    print('Игрок 1 победил')
elif matem == 'бумага' and first == 'камень':
    print('Игрок 2 победил')
elif matem == 'бумага' and first == 'бумага':
    print('ничья')
elif matem == 'бумага' and first == 'ножница':
    print('Игрок 1 победил')
elif matem == 'ножница' and first == 'камень':
    print('Игрок 2 победил')
elif matem == 'ножница' and first == 'ножница':
    print('ничья')
elif matem == 'ножница' and first == 'бумага':
    print('Игрок 1 победил')
else:
    print('Ошибка!')



# Вторая пройденная тема for и in в кодинге, а также цикл while
numbers = int(input("Введите число: "))
for i in range(1, 11):
    print(numbers, "x", i, "=", numbers * i)

# Третий урок так же циклы
numbers = [i for i in range(1,21)]
chotnie1 = [num for num in numbers if num % 2 == 0]
print(chotnie1)

# Dictionary
my_dict = {'name': 'Jordan'}
my_dict['name'] = 'Pasha'
print(my_dict)

# Функция Def
def say_hello():
    print('Hello World')
say_hello()

# lambda = мини функция для легких задач
a = lambda x:x**2
print(a(10))

# class и self с функцией
class MyClass:
    def __init__(self, name):
        self.name = name

# Так же класс и функции
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

# работа с сайтом git и github
# git init
# git add
# git push
# git branch
# git merge
# git pull


#SQL база данных
# SQL данные
# integer = целые числа
# real = десятичные дроби (float)
# text = текстовые значения (str)
# import sqlite3
# sqlite3.connect('card.db')

