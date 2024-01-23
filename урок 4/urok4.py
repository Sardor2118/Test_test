names = []
number = []
service = []

while True:
    action = input("Введите действие: имя, номер, сервис, выход: ")
    if action.lower() == 'имя':
        new_name = input("Введите новое имя: ")
        if new_name in names:
            print("Такое имя уже занято")
        else:
            names.append(new_name)
            print(f'{new_name} добавлен в список')
        print(names)
    elif action.lower() == 'номер':
        new_number = input("Введите новый номер: ")
        if new_number in number:
            print("Такой номер уже занято")
        else:
            number.append(new_number)
            print(f'{new_number} добавлен в список')
        print(number)
    elif action.lower() == 'сервис':
        new_service = input("Введите новый сервис: ")
        if new_service in service:
            print("Такой сервис уже есть")
        else:
            service.append(new_service)
            print(f'{new_service} добавлен в список')
        print(service)
    elif action.lower() == 'выход':
        break
    else:
        print('Такой функции нет')
        break