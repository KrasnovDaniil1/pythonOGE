
# * округление
# x = 6.5
# round_x = round(x)
# print(f"Округление {x} это {round_x}")

# * модуль
x = -42.42
abs_x = abs(x)
print(f"Абсолютное значение {x} это {abs_x}")

# * Импорт модулей
# import math
# from math import ceil, floor
# from math import *

# ? 1. МОДУЛЬ math — математические функции

# * 1. Константы
print(f"Число Пи: {math.pi}")           # 3.141592653589793

# * 2. Округление
print(f"Вверх (ceil): {math.ceil(4.2)}")      # 5
print(f"Вниз (floor): {math.floor(4.9)}")     # 4

# * 3. Логарифмы
print(f"Логарифм по основанию 2: {math.log2(8)}")   # 3.0
print(f"Логарифм с произвольным основанием: {math.log(8, 2)}")  # 3.0

# ? 2. МОДУЛЬ random — случайные числа
from random import *

# * генерирует случайное целое число N в диапазоне от a до b включительно
print(f"randint(1, 6): {randint(1, 6)}")    # от 1 до 6 (как кубик)