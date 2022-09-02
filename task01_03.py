# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
#             номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# Solution

def quarter_search(x, y):
    while True:
        if x > 0 and y > 0:
            print("I четверть!")
            break
        elif x < 0 and y > 0:
            print("II четверть!")
            break
        elif x < 0 and y < 0:
            print("III четверть!")
            break
        elif x > 0 and y < 0:
            print("IV четверть!")
            break
        else:
            print("Введите X !=0 and Y !=0 ")
            x = int(input("X = "))
            y = int(input("Y = "))


quarter_search(0, 0)
