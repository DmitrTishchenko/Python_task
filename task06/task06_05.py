# 5 - Найти произведение пар чисел в списке.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import function as fun
from typing import List
import os
os.system('cls||clear')

list_number = fun.get_list(fun.get_number(
    'Введите целое число для рандомного списка: \n'))
print(f'Рандомный список:\n', list_number)
list_result = [list_number[i] * list_number[-1-i]
               for i in range(len(list_number)//2 + len(list_number) % 2)]
print(f'Сумма пар элементов:\n', list_result)
