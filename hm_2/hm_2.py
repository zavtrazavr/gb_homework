# Задание 1

def input_div(x, y):
    try:
        res = x/y
    except ZeroDivisionError as err:
        res = err
    return res

print(input_div(20,5))


# Задание 2

def user(name, lastname, birth_year, city, email, phone_num):
    return f'Имя: {name}, фамилия: {lastname}, год рождения: {birth_year}, город: {city}, email: {email}, номер телефона: {phone_num}'

print(user(name='Даша', lastname= 'Алешина', city='Москва', birth_year=1991, phone_num=9997777777, email='blabla@mail.ru'))


# Задание 3

def my_func(x, y, z):
    my_list = [x, y, z]
    my_list = sorted(my_list, reverse=True)
    return my_list[0] + my_list[1]

print(my_func(1,2,3))


# Задание 4

def my_func(x, y):
    y = abs(y)
    mult = x
    while y > 0 and y != 1:
        mult *= x
        y = y - 1
    return 1/mult


print(my_func(0.1,-1))


# Задание 5

def input_sum(*nums):
    inp_sum = 0

    for num in nums:
        inp_sum += num
    return inp_sum


summa = 0
while True:
    inp = input('Введите числа через пробел\n')
    inp = inp.split()

    if not inp or not inp[0].isalnum():
        break

    else:
        for i in range(len(inp)):
            if not inp[i].isalnum():
                inp.pop(i)

        inp = list(map(int, inp))
        a = input_sum(*inp)
        summa += a

    print(summa)


# Задание 6

def int_func(text):
    return text.capitalize()

#print(int_func('lala'))


inp = input('Введите список слов маленькими буквами через пробел\n')
inp = inp.split()

for i in range(len(inp)):
    inp[i] = int_func(inp[i])
print(', '.join(inp))