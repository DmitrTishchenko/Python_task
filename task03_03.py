# 3-Задайте список из вещественных чисел. Напишите программу,
#   которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

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
    Создаем список вещественных чисел
    '''
    list_number = [round(random.random()*10, 2) for _ in range(number)]
    return list_number


def difference_numbers(list_number: List) -> int:
    '''
    Получение разницы между максимальным и минимальным 
    значением дробной части элементов списка. 
    '''
    list_new = [i % 1 for i in list_number]
    difference = int(((max(list_new)*100) - (min(list_new))*100))
    return difference


one_number = get_number('Введите целое число: ')
list_numbers = get_list(one_number)
print(list_numbers)
print('max-min:')
print(difference_numbers(list_numbers))
