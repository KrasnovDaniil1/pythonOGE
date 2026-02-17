# ? цикл while
# * 1. цикл работает пока условие истинно
# while True:
#     print("hello")

# * добавляем счетчик
i = 0
while i < 5:
    print(f"Итерация: {i}")
    i += 1

# * счетчик от и до
i = 5
while i < 10:
    print(f"Итерация: {i}")
    i += 2

# * пример
num = int(input("Введите стоимость товара, 0 - завершить"))
total = 0
while num != 0:
    total += num
    print(f"Итого: {total}")
    num = int(input("Введите стоимость товара, 0 - завершить"))

