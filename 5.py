# ? составные выражения / (and, or)

# * Оператор and (И) Выражение истинно, только если ОБА условия верны
age = 25
balance = 1000
if age >= 18 and balance > 500:
    print("Покупка разрешена")
else:
    print("Недостаточно средств или мал возраст")

# * 2. Оператор or (ИЛИ) Выражение истинно, если ХОТЯ БЫ ОДНО из условий верно
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Сегодня выходной")
else:
    print("Сегодня рабочий день")


# * Оператор not (НЕ) Инвертирует (переворачивает) результат условия
is_banned = False
if not is_banned:
    print("Доступ разрешен. Вы не забанены.")
else:
    print("Доступ к ресурсу запрещен.")


# ? вложенные конструкции / nested structures
username = "admin"
password = "1234"
if username == "admin":
    print("Логин найден.")
    if password == "1234":
        print("Пароль верный. Вход выполнен!")
    else:
        print("Неверный пароль.")
else:
    print("Такого пользователя не существует.")


# ! Важно помнить порядок выполнения (приоритет):
# * not (выполняется первым)
# * and (выполняется вторым)
# * or (выполняется последним)
# * Скобки () меняют этот порядок.


# ? задачи
x,y,z = True, False, True
print(x or y and z)
print(x and y or x)
print(not x or y and z)
print(not x and not y or z)
print(x and x or y and x or x)
print((x or y) and (not z))