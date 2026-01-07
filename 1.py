# print() выводит данные на экран
print("Hello world!") # двойные кавычки
print('Hello world!') # одинарные кавычки
print(2026) # 2026
print (2026 + 4) # 2030
print("Итого:", 500, "руб")

# комментарий

# переменная
name = "Алекс"
print("Воин", name)
print(f"Воин {name}")

num1 = 5
num2 = 10
total = num1 + num2
print(total)

num = 5 # меняем значение
print(num)
num = 10
print(num)

num1, num2 = 5, 10
print(num1, num2)


# Правила наименования переменных
# Только латинские символы от a-z A-Z
# Цифры, но не на первой позиции
# Разрешен символ _
client1 = 1
client2 = 2
# 1car = 5 ошибка
# Нельзя использоват зарезервированные имена 
# print = 10 нельзя


# snake_case - рекомендован
client_name = "Иван"
ticket_price = 200


# camelCase
clientName = "Иван"
ticketPrice = 200


# Типы данных - у каждого своё предназначение
# integer / int / целое число
my_int = 10
print(my_int, type(my_int)) 


# float / float / дробное число
my_float = 10.5
print(my_float, type(my_float))


# string / str / строка
my_str_1 = 'Hello1'
print(my_str_1, type(my_str_1))
my_str_2 = "Hello2"
print(my_str_2, type(my_str_2))
my_str_3 = "Иван сказал: '...'"
print(my_str_3, type(my_str_3))
my_str_4 = 'Иван сказал: "..."'
print(my_str_4, type(my_str_4))


# boolean / bool / логический тип
my_bool_1 = True
print(my_bool_1, type(my_bool_1))
my_bool_2 = False
print(my_bool_2, type(my_bool_2))


# list / list / список - хранит упорядоченные значения
my_list = ['Sasha', 20, 170.5]
print(my_list, type(my_list))


# tuple / tuple / кортеж - после создания нельзя изменить
my_tuple = (19, 'hello', 8.9)
print(my_tuple, type(my_tuple))


# set / set / множества - хранит только уникальные значения
my_set = {1, 1, 1, 1, 2 , 3, 2, 4}
print(my_set, type(my_set))


# dictionary / dict / словарь
my_dict = {'name': 'Egor', 'age': 17, 'height': 180}
print(my_dict, type(my_dict))


# input - считывает данные введенные пользователем, 
name = input() # всегда возвращает строку
print(name, type(name))
surname = input('Введите фамилию:') # можно указать подсказку
print(name, type(name))
age = input('Введите возраст:') # всегда возвращает строку
print(age, type(age))


# int - переводит в числовый тип данных
str_in_int = int('5') 
print(str_in_int, type(str_in_int))

str_in_int = int(5.0)
print(str_in_int, type(str_in_int))

str_in_int = int('привет') # ошибка


# str - переводит в строковый тип данных
int_in_str = str(5)
print(int_in_str, type(int_in_str))














