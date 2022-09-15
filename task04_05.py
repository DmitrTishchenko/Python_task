# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия
#  и восстановления данных. Входные и выходные данные хранятся в
# отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.


def rle(str):
    result = []
    count = 0

    if len(str) == 1:
        result.append((1, int(str[0])))
        return result

    for i in range(len(str)):
        count += 1
        if (i + 1) == len(str) or str[i] != str[i + 1]:
            result.append((count, str[i]))
            count = 0

    return result


if __name__ == "__main__":

    str = input()
    result = rle(str)

    for amount, figure in result:
        print(amount, figure)
