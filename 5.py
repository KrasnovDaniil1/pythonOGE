# ? составные выражения / (and, or)

# * 1. Оператор and (И) Выражение истинно, только если ОБА условия верны
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
