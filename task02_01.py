# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

def count_number():
    try:
        number = input('Введите число: ')
        number_list = list(int(i) for i in number if i != '-' and i != '.')
        return sum(number_list)
    except (ValueError):
        return count_number()


result = count_number()
print(f'Сумма чисел введеного числа = {result}')
