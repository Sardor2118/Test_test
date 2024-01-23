def say_hello():
    print('Hello World')
say_hello()

# def название_функции():
    # код для этой функции
#вызов функции

def name():
    a = 1
    b = 2
    c = a + b
    return c
print()

def spam2(a):
    print(a+6)
spam2(3)

def spam2(a, b, c=0, d=0, e=0):
    print(a+b+c+d+e)

spam2(3,5, 8, 0, 4)

def qwe(a, s):
    print(a+s)
qwe(21, 18)

all_products = {'Склад': {'name': 'Хлеб', 'количество': 34}}
def get_products(a):
    print(all_products['Склад'][a])
get_products('name')

def spam1(*args):
    return args

print(spam1(1, 2, 3, 4, 'Hello'))
print(type(spam1()))

def spam(**kwargs):
    return kwargs
print(spam(name='my1', age=23))

def spamm(**kwargs):
    for k,v in kwargs.items():
        return k,v
print(spamm(name='my2', age=20))


#имортирует код сайта из ссылки
#import requests
#response = requests.get('https://fpdl.in/')
#print(response.text)


hotel = {}

def add_client():
    room_numbers = list(hotel.values())
    print("Занятые номера:", room_numbers)
    name = input("Введите имя клиента: ")
    room_number = input("Введите номер комнаты: ")
    hotel[name] = room_number
    print("Клиент успешно добавлен.")

def remove_client():
    name = input("Введите имя клиента: ")
    if name in hotel:
        del hotel[name]
        print("Клиент успешно удален.")
    else:
        print("Клиент не найден.")

def show_rooms():
    room_numbers = list(hotel.values())
    print("Занятые номера:", room_numbers)

while True:
    print("1. Добавить клиента")
    print("2. Удалить клиента")
    print("3. Увидеть занятые номера")
    print("4. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        add_client()
    elif choice == "2":
        remove_client()
    elif choice == "3":
        show_rooms()
    elif choice == "4":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
