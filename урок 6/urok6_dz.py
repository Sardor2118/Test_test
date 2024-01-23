all_products = {'Весь склад': {}}
korzina = []
while True:
    menu = input('Что вы хотите сделать? \n'
                 '1- добавить продукт \n'
                 '2- посмотреть весь склад \n'
                 '3- корзина для покупок \n'
                 '4- удалить из корзины \n'
                 '5- изменить товары в корзине ')
    if menu == '1':
        product_name = input('Введите название продукта: ')
        product_count = input('Введите количество продукта: ')
        all_products['Весь склад'][product_name] = product_count
    elif menu == '2':
       #print(all_products)
        for k, v in all_products['Весь склад'].items():
            print(f'Название продукта {k}\n'
                  f'Количество: {v}')
    elif menu == '3':
        while True:
            chto_kupit = input('Что купить? ')
            korzina.append(chto_kupit)
            print(f'Нужно купить: {chto_kupit}')
            print(korzina)
            a = input()
            if a.lower().replace(" ", "") == 'выйти':
                break
    elif menu == '4':   
        print(korzina)
        deleting = input('Введите продукт чтобы удалить из корзины: ')
        if deleting in korzina:
            korzina.remove(deleting)
            print(korzina)
        else:
            print('Нету этого продукта в корзине')
    elif menu == '5':
        print(korzina)
        change = input('Введите какой продукт хотите заменить: ')
        change2 = input('Введите замену: ')
        index1 = korzina.index(change)
        korzina[index1] = change2
        print(korzina)
        print('Продукт успешно изменён!')
       # else:
       # print('Нету этого продукта в корзине')
    else:
        print('Повторите попытку')