# 1 - Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


import os
os.system('cls||clear')


def get_number(input_string: str) -> int:
    '''
    Получение целого числа
    '''
    while True:
        try:
            number = int(input(input_string))
            return number
        except ValueError:
            print('Давайте сначала! ')


def list_mnoj(number: int):
    list_mnoj_ot_number = []
    for i in range(2, number+1):
        if i > 1 and (i % 2 != 0 or i == 2) and (i % 3 != 0 or i == 3) and number % i == 0:
            list_mnoj_ot_number.append(i)
    return list_mnoj_ot_number


N = get_number('Введите целое чило ')
print(f'Список простых множетелей числа', N, 'это:', list_mnoj(N))
