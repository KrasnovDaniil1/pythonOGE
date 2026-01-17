# ? boolean / bool / логический тип
my_bool_1 = True
print(my_bool_1, type(my_bool_1))
my_bool_2 = False
print(my_bool_2, type(my_bool_2))

# ? логические операторы
print(5 > 3) # * больше
print(5 >= 3) # * больше и равно
print(5 < 3) # * меньше
print(5 <= 3) # * меньше и равно
print(5 == 3) # * равно
print(5 != 3) # * не равно

# ? условные операторы / if-elif-else
# * 1. if (если)
num = 10
if num > 0:
    print("Число положительное")
# * 2. Конструкция if-else (если-иначе)
age = 15
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
# * 3. Конструкция if-elif-else (если - иначе если - иначе)
traffic_light = "yellow"
if traffic_light == "green":
    print("Едем")
elif traffic_light == "yellow":
    print("Ждем")
else:
    print("Стоим")