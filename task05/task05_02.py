# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите).
# Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем
# 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.


import random
import os
os.system('cls||clear')


def get_number(input_string: str) -> int:
    '''
    Получение кол-ва конфет
    '''
    while True:
        try:
            num = int(input(input_string))
            if 0 < num < 29:
                return num
            else:
                print('Вы вводите не то число!')
        except ValueError:
            print('Ну это совсем не то что мы хотим от вас увидеть')


def last_move(input_string: str, number: int) -> int:
    '''
    Получение кол-ва конфет
    для последнего хода
    '''
    while True:
        try:
            num = int(input(input_string))
            if 0 < num <= number:
                return num
            else:
                print('Вы вводите не то число!')
        except ValueError:
            print('Ну это совсем не то что мы хотим от вас увидеть')


def get_player(player_1: str, player_2: str) -> str:
    '''
    Получение имени игроков
    определение первого хода
    '''
    print('Сейчас мы разыграем право первого хода...')
    temp = random.randint(0, 1)
    if temp == 0:
        gamer = player_1
    else:
        gamer = player_2
    print(f'И первым у нас берет конфеты {gamer}!')
    return gamer


def playng(candy: int, player: str, player_1: str, player_2: str) -> str:
    winner = ''
    while candy > 0:
        if candy > 28:
            if player == player_1:
                print(f'У нас {candy} конфет.')
                move = get_number(
                    f'{player} сколько вы берете кофет? Вы можете взять от 1 до 28: ')
                candy -= move
                player = player_2
                winner = player_1
            else:
                print(f'У нас {candy} конфет.')
                move = get_number(
                    f'{player} сколько вы берете кофет? Вы можете взять от 1 до 28: ')
                candy -= move
                player = player_1
                winner = player_2
        else:
            if player == player_1:
                print(f'У нас {candy} конфет.')
                move = last_move(
                    f'{player} сколько вы берете кофет? Вы можете взять от 1 до {candy}: ', candy)
                candy -= move
                player = player_2
                winner = player_1
            else:
                print(f'У нас {candy} конфет.')
                move = last_move(
                    f'{player} сколько вы берете кофет? Вы можете взять от 1 до {candy}: ', candy)
                candy -= move
                player = player_1
                winner = player_2
    return winner


ran_sweet = random.randint(50, 100)
print(f'''
Добро пожаловать в игру
На столе лежит {ran_sweet} конфета.
Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Выигрывает игрок сделавший последний ход 
- он забирает все конфеты.\n''')

name_1 = input('Давайте знакомиться. Первый игрок, как к Вам обращаться?\n')
name_2 = input('Второй игрок, представтесь, пожалуйста:\n')
gamer = get_player(name_1, name_2)
sweet = ran_sweet
winner = playng(sweet, gamer, name_1, name_2)
print(f'''
У нас есть победитель.
Это игрок с именем {winner}!!!
Наша игра закончена.''')
