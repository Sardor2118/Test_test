#Создание списка квадратов чисел от 1 до 5:
squares = [x**2 for x in range(1, 6)]
print(squares)

#Создание списка четных чисел от 0 до 10:
evens = [x for x in range(11) if x % 2 == 0]
print(evens)

#Создание списка букв из строки:
letters = [letter for letter in 'hello']
print(letters)

#Создание списка чисел, которые делятся на 3 или на 5:
numbers = [x for x in range(1, 11) if x % 3 == 0 or x % 5 == 0]
print(numbers)

#Создание списка квадратов чисел, которые делятся на 2:
squares2 = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares2)

#Создание списка чисел, которые не являются четными:
odds = [x for x in range(11) if x % 2 != 0]
print(odds)

#Создание списка чисел, которые больше 5:
numbers = [x for x in range(10) if x > 5]
print(numbers)