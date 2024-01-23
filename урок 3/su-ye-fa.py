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