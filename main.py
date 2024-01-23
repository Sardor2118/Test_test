first = int(input('Введи первое число'))
matem = input('(+ - * /) ')
second = int(input('Введите второе число'))

# если в тексте переменной matem есть '+'
if matem == '+':
    print(first+second)
elif matem == '-':
    print(first-second)
elif matem == '*':
    print(first*second)
elif matem == '/':
    print(first/second)
else:
    print('Не верное значение')