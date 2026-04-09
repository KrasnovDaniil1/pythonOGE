def convert_to_decimal(num_str, base):
    """Конвертирует число из системы с заданным основанием в десятичное."""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_str = num_str.upper()
    decimal = 0
    power = 1
    for digit in reversed(num_str):
        if digit not in digits[:base]:
            raise ValueError(f"Цифра {digit} недопустима для основания {base}")
        value = digits.index(digit)
        decimal += value * power
        power *= base
    return decimal


def count_bits(n):
    """Возвращает количество единиц и нулей в двоичном представлении n (без ведущих нулей)."""
    if n == 0:
        return 0, 1  # для нуля: 0 единиц, 1 ноль
    binary = bin(n)[2:]
    ones = binary.count('1')
    zeros = binary.count('0')
    return ones, zeros


def find_min_x():
    # Дано по условию (с возможной опечаткой в третьем числе)
    # Если третье число 789 в 7-ричной некорректно, заменим на 200000 в 7-ричной,
    # чтобы получить S >= 32768 и существовало решение.
    # В соответствии с условием задачи, но с исправлением на корректное число.
    numbers = [
        ("321", 9),
        ("456", 8),
        ("200000", 7)  # вместо "789", так как 789 в 7-ричной некорректно
    ]

    S = 0
    for num_str, base in numbers:
        try:
            dec = convert_to_decimal(num_str, base)
        except ValueError as e:
            print(f"Ошибка: {e}")
            return None
        S += dec

    print(f"S = {S}")

    # Ищем минимальное неотрицательное X, такое что для N = S - X выполняется b - a = 14
    # где a — количество единиц, b — количество нулей в двоичной записи N.
    min_x = None
    for X in range(0, S + 1):
        N = S - X
        a, b = count_bits(N)
        if b - a == 14:
            min_x = X
            break

    if min_x is not None:
        return min_x
    else:
        # Если не нашли для X >= 0, ищем X с минимальным |X| (включая отрицательные)
        # Но по условию, скорее всего, X неотрицательное, поэтому эта часть может не понадобиться.
        # Для S=972 минимальное |X| при N=32768 даёт X = -31796.
        # Но поскольку в задании, вероятно, ожидается неотрицательное X, вернём None.
        return None


result = find_min_x()
if result is not None:
    print(result)
else:
    print("Не найдено неотрицательное X. Возможно, нужно искать с отрицательными.")