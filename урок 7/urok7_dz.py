school = {}

def add():
    class_numbers = list(school.values())
    print("Занятые классы:", class_numbers)
    name = input("Введите имя ученика: ")
    class_numbers = input("Введите номер класса: ")
    school[name] = class_numbers
    print("Ученик успешно добавлен.")

def remove():
    name = input("Введите имя ученика: ")
    if name in school:
        del school[name]
        print("Ученик успешно удален.")
    else:
        print("Ученик не найден.")

def show():
    class_numbers = list(school.values())
    print("Занятые классы:", class_numbers)

while True:
    print("1. Добавить ученика")
    print("2. Удалить ученика")
    print("3. Увидеть занятые классы")
    print("4. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        add()
    elif choice == "2":
        remove()
    elif choice == "3":
        show()
    elif choice == "4":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
