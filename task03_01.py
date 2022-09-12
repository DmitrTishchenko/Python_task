# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#    стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

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
    list_number = [random.randint(-10, 10) for _ in range(number)]
    return list_number


def sum_number(list_number: List) -> int:
    '''
    Сумма элементов нечётных позиций
    '''
    new_list = [list_number[i] for i in range(len(list_number)) if i % 2 != 0]
    return sum(new_list)


one_number = get_number('Введите целое число: ')
list_numbers = get_list(one_number)
print(list_numbers)
result = sum_number(list_numbers)
print("Сумма нечётных элементов")
print(result)
