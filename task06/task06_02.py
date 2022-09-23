# 2- Найти сумму чисел списка стоящих
# на нечетной позиции

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9,
# ответ: 12

import function as fun
import os
os.system('cls||clear')


number = abs(fun.get_number(
    'Введите размер списка, это должно быть целое число: '))
list_1 = fun.get_list(number)
result_list = [v for i, v in enumerate(list_1) if i % 2]
result = sum(result_list)

print('Список элементов:\n', list_1)
print('Список элементов стоящих на нечетных позициях: \n', result_list)
print('Сумма = ', result)
