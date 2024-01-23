# написать приложение, которое будет считать стоимость бутылок, сдаваемых для переработки
small_bottle_cost = 0.10
large_bottle_cost = 0.25

small_bottles = int(input('Введите количество бутылок объемом 1 литр и меньше: '))
large_bottles = int(input('Введите количество бутылок большего объема: '))
math = small_bottles * small_bottle_cost + large_bottles * large_bottle_cost
print(f'Вы можете получить ${math:.2f} если сдадите все бутылки')
#round(Число, количество цифр после запятой)


# написать приложение которое посчитает чаевые(18%) официанту и стоимость налога(12%)
check = int(input('Напишите сумму заказа в ресторане: '))
nds = check * 0.12
tips = check * 0.18
print(f'Сумма НДС получится: {nds:.2f}')
print(f'Сумма чаевых получится: {tips:.2f}')
total = check + nds + tips
print(f'Общая сумма для оплаты: {total:.2f} ')



# написать программу, посчитать сумму положительных чисел от 1 до n

numbers = int(input('Введите натуральное положительное число: '))
if numbers > 0:
    s = 0
    for i in range(1, numbers + 1):
        s += i
    print(f'Сумма натуральных чисел от 1 до {numbers} равна {s}')
else:
    print('Неверный ввод. Пожалуйста, введите натуральное положительное число')


# написать код для интернет магазина, расчитать общий вес посылки, сувенир 75гр и безделушка 112гр

suvenir = 0.075
bezdelushka = 0.112
quantity_suvenir = int(input('Напишите количество сувениров: '))
quantity_bezdelushka = int(input('Напишите количество безделушек: '))
quantity_total = suvenir * quantity_suvenir + bezdelushka * quantity_bezdelushka
print(f'Общий вес посылки {quantity_total} грамм')