from sys import argv
from random import randint
from functools import reduce
from itertools import count, cycle


# Задание 1

def counter(hours, rate, prize):
    return (hours*rate) / prize


print(counter(int(argv[1]), int(argv[2]), int(argv[3])))


# Задание 2

a = [randint(1, 500) for i in range(10)]
b = []

for i in range(len(a)-1):
    if a[i+1] > a[i]:
        b.append(a[i+1])

print(b)


# Задание 3

a = [x for x in [i for i in range(20, 240)] if (x % 20 == 0 or x % 21 == 0)]

print(a)


# Задание 4

a = [randint(1, 20) for i in range(1, 20)]
b = [x for x in a if a.count(x) == 1]

print(a)
print(b)


# Задание 5

a = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda i, j: i*j, a))


# Задание 6

for x in count(5):
    if x > 20:
        break
    else:
        print(x)



c = 0
for x in cycle([i for i in range(2, 5)]):
    if c > 10:
        break
    print(x)
    c+= 1


# Задание 7

def fuct(n):
    i = 1
    j = 1
    while i <= n:
        j *= i
        i += 1
        yield j


for el in fuct(5):
    print(el)