data = {'name': 'Jordan', 'age': 12, 'job': 'python programmer'}
print(data['name'], data['job'])

data2 = {'name1': ['Jordan', 'Pavel'], 'age': (12, 21), 'job1': 'programmers'}
print(data2['name1'][0], data2['job1'][-1])

data3 = {'name1': ['Jordan', 'Pavel'], 'age': (12, 21), 'job1': 'programmers'}
print(data3.items())

instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
a = instructor.values()
b = instructor.items()
c = instructor.keys()
if 'Jordan' in instructor.keys() and instructor.values():
    print('Да есть')
else:
    print('Нету')

my_dict = {'name': 'Jordan'}
my_dict['name'] = 'Pasha'
print(my_dict)

dict().fromkeys('a', 1)
# {}.fromkeys(['a'], 1)
print({}.fromkeys('song', 'Godzila'))

my2 = {'title': 'Python for'}
print(my2.get('title'))

sas = dict(name='Jordan', job='Developer', age=23)
sas2 = sas.copy()
print(sas2)

namess = {'Names', 1, 2, 3, 4, 5}
print(namess)

nums = [1, 2, 3, 4, 4, 5, 5]
print(set(nums))

nums1 = [1, 2, 3, 4, 4, 5, 5]
for i in set(nums1):
    print(i)

nums1 = {'name': 'Jordan', 'age': 25}
for i in nums1.values():
    print(i)

# можно выбрать 2 значения и ключ сразу же. через .items
nums1 = {'name': 'Jordan', 'age': 25}
for k, v in nums1.items():
    print(k, v)


#.get чтобы не выводил ошибку, а вместо него писал none когда нет товара