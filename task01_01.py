# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# Solution

day_of_the_week = int(input("Введите день недели от 1 до 7 "))
while True:
    day_of_the_week < 7 and day_of_the_week > 0
    if day_of_the_week == 1:
        print("Понедельник, рабочий день!")
        break
    elif day_of_the_week == 2:
        print("Вторник, более интенсивный рабочий день!")
        break
    elif day_of_the_week == 3:
        print("Среда, все еще работаем..")
        break
    elif day_of_the_week == 4:
        print("Четверг, РАБОЧИЙ")
        break
    elif day_of_the_week == 5:
        print("Пятница, полурабочий")
        break
    elif day_of_the_week == 6:
        print("Суббота, да! Выходной")
        break
    elif day_of_the_week == 7:
        print("Воскресенье, да! Выходной")
        break
    else:
        day_of_the_week = int(input("Введите день недели от 1 до 7!!! "))
