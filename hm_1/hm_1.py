# # This is a sample Python script.
#Задание 1
test_1 = input('Введите строковую тестовую переменную\n')
test_2 = int(input('Введите целое число\n'))

print(test_1)
print(test_2)


#Задание 2
inp = int(input('Введите время в секундах\n'))

a = inp // 3600
hr = str(a // 10) + str(a % 10)
b = (inp - (a*3600)) // 60
min = str(b // 10) + str(b % 10)
c = (int(inp) - (a*3600) - (b*60))
sec = str(c // 10) + str(c % 10)

print (f'{hr}:{min}:{sec}')


#Задание 3
inp = input('Введите число\n')
a = int(inp) + int(inp + inp) + int(inp + inp + inp)

print(a)


# Задание 4
inp = int(input('Введите целое положительное число\n'))

max = 0

while inp > 0:
    curr_val = inp % 10
    if curr_val > max:
        max = curr_val
    inp = inp // 10

print(f'Самая боьшая цифра в числе: {max}')


#Задание 5
earn = int(input('Введите значение выручки\n'))
expense = int(input('Введите значение издержек\n'))

if earn - expense > 0:
    a = 'прибыль'
else:
    a = 'убытки'

print(f'Финансовая модель: {a}')

if a == 'прибыль':
    print(f'Рентабельность выручки: {earn/(earn-expense)}')
    count = int(input('Введите количество сотрудников\n'))
    print(f'Прибыль фирмы в расчете на сотрудника: {(earn-expense)/count}')

#Задание 6

a = float(input('Введите км в день\n'))
b = float(input('Введите общее км\n'))

c = 1
while b-a >= 0:
    a = a+0.1*a
    c = c+1
    print(a)
print(c)