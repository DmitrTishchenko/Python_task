# 6 - Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import function as fun
import os
os.system('cls||clear')

N = fun.get_number('Введите число N: \n')
list_result = [(-3) ** i for i in range(N)]
print(list_result)
