
# * округление
# x = 6.5
# round_x = round(x)
# print(f"Округление {x} это {round_x}")

# * модуль
x = -42.42
abs_x = abs(x)
print(f"Абсолютное значение {x} это {abs_x}")

# * Импорт модулей
import math
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

# ! Важно: все тригонометрические функции работают с РАДИАНАМИ, не градусами!

# * 4 Конвертация градусов в радианы и обратно
angle = 45
angle_rad = math.radians(angle)
print(f"{angle}° = {angle_rad} радиан")

# * 5 Синус (sin)
print(f"\n--- Синус ---")
print(f"sin(0°) = {math.sin(math.radians(0))}")       # 0.0
print(f"sin(30°) = {math.sin(math.radians(30))}")     # 0.5
print(f"sin(45°) = {math.sin(math.radians(45))}")     # 0.7071
print(f"sin(90°) = {math.sin(math.radians(90))}")     # 1.0

# * 6 Косинус (cos)
print(f"\n--- Косинус ---")
print(f"cos(0°) = {math.cos(math.radians(0))}")       # 1.0
print(f"cos(60°) = {math.cos(math.radians(60))}")     # 0.5
print(f"cos(45°) = {math.cos(math.radians(45))}")     # 0.7071
print(f"cos(90°) = {math.cos(math.radians(90))}")     # ≈ 0 (очень маленькое число)

# * 7 Тангенс (tan)
print(f"\n--- Тангенс ---")
print(f"tan(0°) = {math.tan(math.radians(0))}")       # 0.0
print(f"tan(45°) = {math.tan(math.radians(45))}")     # 1.0
print(f"tan(60°) = {math.tan(math.radians(60))}")     # 1.7321
# ! tan(90°) — не существует (деление на ноль)

# * 8 Котангенс (ctg) — в Python нет встроенной функции!
# * Формула: ctg(x) = 1 / tan(x)  или  ctg(x) = cos(x) / sin(x)
print(f"\n--- Котангенс ---")
x = math.radians(45)
print(1 / math.tan(x))
print(math.cos(x) / math.sin(x))

# ! ctg(0°) и ctg(180°) — не существуют




# ? 2. МОДУЛЬ random — случайные числа
from random import *

# * генерирует случайное целое число N в диапазоне от a до b включительно
print(f"randint(1, 6): {randint(1, 6)}")    # от 1 до 6 (как кубик)