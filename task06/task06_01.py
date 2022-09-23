# 1 - Определить, присутствует ли в заданном списке строк, некоторое число

import function as fun
import os
os.system('cls||clear')

number_list = fun.get_number('Введите размер списка: \n')
list_new = fun.get_list(number_list)
print(f'Рандомный список:\n', list_new)
number = fun.get_number('Введите искомое число: \n')
have_numbers = [l for x in str(list_new) for l in x if l == str(number)]


if len(have_numbers) == 0:
    print(f'{number} этого числа нет в списке')
else:
    print(f'{number} это число есть в списке')
