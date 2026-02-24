# ? break, continue и else в циклах (for else / while else)


# * 1. break — полностью прерывает цикл
while True:
    num = int(input("Введите число (0 - выход): "))
    if num == 0:
        print("Выход из цикла")
        break          # сразу выходим из цикла
    print(f"Вы ввели: {num}")


# * 2. continue — пропускает остаток текущей итерации
# * Выводим только нечётные числа от 1 до 10
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue      # пропускаем чётные числа
    print(f"Нечётное число: {i}")


# * 3. for else — else выполняется, если не было break
for num in range(7):
    if num == 8:
        print("Нашли число 8!")
        break
    print(f"Проверяем: {num}")
else:
    print("Число 8 не найдено в списке")


# * 4. while else — выполняется, если не было break
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Цикл завершился нормально (без break)")


# *  break + else:
i = 0
while i < 5:
    if i == 3:
        print("Достигли 3, выходим через break")
        break
    print(i)
    i += 1
else:
    print("Цикл завершился без break")