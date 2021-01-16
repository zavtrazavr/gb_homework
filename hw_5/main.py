# Задание 1

data = open('ex_1.txt', 'w')
while True:
    inp = input('Введите строку\n')
    if not inp:
        break
    else:
        data.write(f'{inp}\n')
data.close()



# Задание 2
with open('ex_2', 'r') as data:
    c_word = 0

    for i, line in enumerate(data):
        word = line.split()
        c_word = len(word)

        print(f'Количество строк в строке {i+1}: {c_word}')
    print(f'Количество строк в файле: {i+1}')


# Задание 3
with open('ex_3', 'r', encoding='UTF-8') as data:
    total_salary = 0

    for i, line in enumerate(data):
        person = line.split()
        if int(person[1]) < 20000:
            print(f'Зарплата меньше 20к: {person[0]}')

        total_salary += int(person[1])

    print(f'Средняя зарплата: {total_salary/(i+1)}')


# Задание 4
num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = open('ex_4_done.txt', 'w', encoding='UTF-8')

source_data = open('ex_4', 'r', encoding='UTF-8')

with source_data:
    line = source_data.readline()
    while line:
        line_lst = line.split()
        line_lst[0] = num_dict.get(line_lst[0])
        line_str = ' '.join(line_lst)
        line = source_data.readline()

        print(line_str)
        new_file.write(f'{line_str}\n')


# Задание 5
from random import randint

source_data = open('ex_5.txt', 'w')

random_lst = [str(randint(1, 100)) for i in range(5)]
source_data.write(' '.join(random_lst))
source_data.close()

with open('ex_5.txt', 'r') as data:
    num_lst = data.read().split()

    summa = 0
    for i in num_lst:
        summa += int(i)
    print(summa)


# Задание 6
import re

res_dict = {}

with open('ex_6', 'r', encoding='UTF-8') as source_data:
    for line in source_data:
        line_lst = line.split()

        summa = 0
        for i in range(1, len(line_lst)):
            cnt = re.findall('\d+', line_lst[i])
            if cnt:
                summa += int(cnt[0])
        res_dict[line_lst[0]] = summa

print(res_dict)


# Задание 7
import json

total_lst = []
firm_dict = {}

with open('ex_7', 'r', encoding='UTF-8') as input_data:

    cnt_positive = 0
    summa = 0

    for line in input_data:
        line_lst = line.split()
        total = int(line_lst[2])-int(line_lst[3])
        #print(f'Прибыль компании {line_lst[0]} = {total}')

        firm_dict[line_lst[0]] = total

        if total > 0:
            summa += total
            cnt_positive += 1

#print(f'Средняя прибыль = {summa/cnt_positive}')
#print(firm_dict)

total_lst.extend((firm_dict, {'avg_profit': summa/cnt_positive}))


with open('ex_7_json.json', 'w') as output_data:
    json.dump(total_lst, output_data)
