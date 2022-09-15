# 2 - Задайте последовательность чисел. Напишите программу,
#     которая выведет список неповторяющихся элементов исходной последовательности.
#     Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]


from ast import List
import random


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


def get_list(number: int) -> List:
    '''
    Создаем список
    '''
    list_number = [random.randint(0, 10) for _ in range(number)]
    return list_number


def get_unique_numbers(list_number):
    unique = []
    for number in list_number:
        if number not in unique:
            unique.append(number)
    return unique


n = get_number('Введите целое число ')
list_number = get_list(n)
print(f'Рандомный список ', list_number)
print(f'Отсортированный список ', get_unique_numbers(list_number))
