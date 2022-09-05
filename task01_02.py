# 2-Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.

# Solution

def table_truth():
    for X in (0, 1):
        for Y in (0, 1):
            for Z in (0, 1):
                if not (X or Y or Z) == (not X and not Y and not Z):
                    print(
                        f' {X}  {Y}  {Z}  {not (X or Y or Z) == (not X and not Y and not Z)} ')
                else:
                    print(
                        f'| {X}  {Y}  {Z}  {not (X or Y or Z) == (not X and not Y and not Z)} ')


print(" X  Y  Z  result")
table_truth()
