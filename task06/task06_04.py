# 4 - Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

from operator import index
import os
os.system('cls||clear')

strings = ['asd', 'sdad', 'qew', '1wazc', 'qwe', 'asd']
search_string = 'asd'

try:
    second_element = [x for x in range(len(strings))[strings.index(
        search_string)+1::] if strings[x] == search_string]
    if second_element:
        print(f'Второе вхождение элемента с индексом: {second_element[0]}')
    else:
        print('Повторения элемента нет')
except ValueError:
    print('Данного элемента нет в списке')
