# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

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


def translation_numbers(namber):
    '''
    Перевод целого числа в двоичное значение
    '''

    n = namber

    b = ''

    while n > 0:
        b = str(n % 2) + b
        n = n // 2

    print(b)


one_number = get_number('Введите целое число: ')
translation_numbers(one_number)
