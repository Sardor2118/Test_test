a = lambda x:x**2
print(a(10))

x = lambda e:e
print(x(9))

b = lambda s:s*s
print(b(20))

c = [1,2,3,'4']
a = map(lambda d:d*2, c)
print(list(a))

cc = [1,2,3,'4']
a = map(lambda d:d*2==4, c)
print(list(a))

ccc = [1,2,3,'4']
a = filter(lambda d:d*2==4, c)
print(list(a))

I = [1,2,3,4,5,6]
a = list(filter(lambda x:x%2 == 0, I))
print(a)

L = ['Jordan', 'Pavel', 'Pasha', 'Jacky']
a = list(filter(lambda x:'J' in x, L))
print(a)

peremena = [1,2, -4, -4, 5, 18, 19, -21]
y = filter(lambda d: d>10, peremena)
print(list(y))
