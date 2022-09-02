# 4- Напишите программу, которая по заданному номеру четверти, показывает диапазон
#    возможных координат точек в этой четверти (x и y).

def range_quarter(number):
    if number == 1:
        print("Диапазон I четверти: х = (0 : + ∞), y = (0 : + ∞)")
    elif number == 2:
        print("Диапазон II четверти: х = (0 : - ∞), y = (0 : + ∞)")
    elif number == 3:
        print("Диапазон IIШ четверти: х = (0 : - ∞), y = (0 : - ∞)")
    elif number == 4:
        print("Диапазон IV четверти: х = (0 : + ∞), y = (0 : - ∞)")


while True:
    number = int(input("Введите номер четверти \n"))
    if number > 0 and number < 5:
        break

range_quarter(number)
