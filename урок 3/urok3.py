contacts = ['Мама', 'Папа']
menu = input('Выберите цифру действия:\n'
             '1- Добавить контакт\n'
             '2- Удалить контакт\n'
             '3- Заменить контакт\n'
             '4- Найти контакт ')
if menu == '1':
    new_name = input('Введите имя нового контакта: ')
    contacts.append(new_name)
    print(contacts)
elif menu == '2':
    deleting = input('Введите имя контакта для удаления ')
    if deleting in contacts:
        contacts.remove(deleting)
        print(contacts)
    else:
        print('Такого контакта нету')
elif menu == '3':
    change = input('Введите имя контакта для замены ')
    change2 = input('Введите новое имя ')
    index1 = contacts.index(change)
    contacts[index1] = change2
    print(contacts)
    print('Контакт успешно изменён')

elif menu == '4':
    find = input('Введите имя контакта ')
    if find in contacts:
         print('Контакт уже существует ')
    else:
         print('Контакт не существует ')
else:
    print('Неверное значение!')