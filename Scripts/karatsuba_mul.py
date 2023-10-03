import math

MULL_TABLE = {}
for i in range(10):
    for j in range(10):
        MULL_TABLE[(i, j)] = i*j


def padZeros(numberString, numZeros, insertSide):
    """Возвращает строку дополненную нулями слева или справа"""
    if insertSide == 'left':
        return '0' * numZeros + numberString
    elif insertSide == 'right':
        return numberString + '0'*numZeros
    else:
        return numberString


def karatsuba(x, y):
    """Перемножаем два целых числа с помощью алгоритма Карацубы.
    Обратите внимание что оператор * не используется."""
    assert isinstance(x, int), 'x must be an integer'
    assert isinstance(y, int), 'y must be an integer'
    x = str(x)
    y = str(y)

    # При получении однозначных чисел находим их в таблице поиска
    if len(x) == 1 and len(y) == 1:  # БАЗОВЫЙ СЛУЧАЙ
        print(f"Lookup {x} * {y} = {MULL_TABLE[(int(x), int(y))]}")
        return MULL_TABLE[(int(x), int(y))]

    print(f"Multiplying {x} * {y}")

    # Дополняем строки X и Y начальными нулями, чтобы они были одинаковой длины
    if len(x) < len(y):
        x = padZeros(x, len(y) - len(x), 'left')
    elif len(y) < len(x):
        y = padZeros(y, len(x) - len(y), 'left')

    # На этом этапе x и y имеют одинаковую длину

    halfOfDigits = math.floor(len(x) / 2)

    # Делим x на половины a и b, а y на с и d
    a = int(x[:halfOfDigits])
    b = int(x[halfOfDigits:])
    c = int(y[:halfOfDigits])
    d = int(y[halfOfDigits:])

    # Выполняем рекурсивные вызовы, передавая эти половины
    step1Result = karatsuba(a, c)  # ?Шаг 1: Перемножение a и c
    step2Result = karatsuba(b, d)  # ?Шаг 2: Перемножение b и d
    # ?Шаг 3: Перемножаем суммы a + b и c + d
    step3Result = karatsuba(a+b, c+d)

    # ?Шаг 4: Вычисляем разность результатов шагов
    step4Result = step3Result - step2Result - step1Result

    # ?Шаг 5: дополняем эти числа нулями и складываем их,
    step1Padding = ((len(x) - halfOfDigits) + (len(x) - halfOfDigits))
    step1PaddedNum = int(padZeros(str(step1Result), step1Padding, 'right'))

    step4Padding = (len(x) - halfOfDigits)
    step4PaddedNum = int(padZeros(str(step4Result), step4Padding, 'right'))

    print(f"Solved {x} * {y} = {step1PaddedNum + step2Result + step4PaddedNum}")

    return step1PaddedNum + step2Result + step4PaddedNum


print(f'1357 * 2468 = {karatsuba(1357, 2468)}')
