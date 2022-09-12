# 2-Напишите программу, которая найдёт произведение пар чисел списка.
#   Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

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


def multiplication_numbers(list_numbers: List) -> None:
    '''
    - делим список на 2 половины
    - перемножаем первый и последний и так далее
    - если сумма элементов нечетная, прибавляем оставшийся элемент 
    '''

    if list_numbers:

        result_list = []
        half_len = len(list_numbers)//2 + len(list_numbers) % 2
        for i in range(half_len):
            result_list.append(list_numbers[i]*list_numbers[-1-i])
        print(result_list)


one_number = get_number('Введите целое число: ')
list_numbers = get_list(one_number)
print(list_numbers)
multiplication_numbers(list_numbers)
