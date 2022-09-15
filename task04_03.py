# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt
#  в одной строке одно число.

import random


def get_number(input_string):
    try:
        num = int(input(input_string))
        return num
    except (ValueError):
        return get_number()


def list_random(num):
    list_element = []
    for i in range(num):
        list_element.append(random.randint(-num, num))
    return list_element


def write_file(num):
    fil = open('file.txt', 'w')
    ind_1, ind_2 = str(random.randint(0, num - 1)
                       ), str(random.randint(0, num - 1))
    fil.write(ind_1)
    fil.write('\n')
    fil.write(ind_2)
    fil.close()


def read_file(list_random):
    r = open('file.txt', 'r')
    index_1, index_2 = int(r.readline()), int(r.readline())
    r.close()
    return list_random[index_1] * list_random[index_2]


number = get_number('Введите количество элементов в списке: ')
list_number = list_random(number)
print('Список: ', list_number)
write_file(number)
number_result = read_file(list_number)
print(f'Произведение элементов =', number_result)
