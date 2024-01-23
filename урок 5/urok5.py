my = ['2', '33', 'Jordan', 'Pavel']
my2 = [i + '2' for i in my]

print(my2[-1])

# условные операторы в List comprehension
nums = [i for i in range(1,11)]
chotnie = [num for num in nums if num % 2 == 0]
nechotnie = [num for num in nums if num % 2 != 0]
print(chotnie, nechotnie)



my = ['2', '33', 'Jordan', 'Pavel']
my2 = [i + '2' for i in my if 'a' in i]

print(my2)


my_list = [i for i in range(1, 11, 2)]
print(my_list)



names = ['Pavel', 'Sasha', 'Jordan', 'Pasha']
answer = [name[0] for name in names]
print(answer)

nums1 = [1,2,3]
my3_list = [a for a in range(1,11) if a in nums1]
print(my3_list)


numbers = [i for i in range(1,21)]
chotnie1 = [num for num in numbers if num % 2 == 0]
print(chotnie1)

usernames = []
while True:
    spisok = input('Введите имя: ')
    if spisok in usernames:
        print('Такой никнейм уже есть')
    else:
        usernames.append(spisok)
        print('Ник добавлен')


