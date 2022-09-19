# 1 - Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

import func
import os
os.system('cls||clear')


name_text = 'task05/task05_01_1.txt'
name_text_2 = 'task05/task05_01_2.txt'
print('Введите текст:')
string_input = input()


func.write_file(string_input, name_text)
string_output = func.read_file(name_text)
string_output = list(filter(lambda x: not 'абв' in x, string_output.split()))
string_output = ' '.join(string_output)
func.write_file(string_output, name_text_2)
