"""Модуль быстрой сортировки 
Алгоритм сортировки разработанный информатикам Тони Хоаром в 1959 году.

"""


def quicksort_egoroff(items: list):
    if len(items) <= 1:
        print(f"Базовый случай: {items}")
        return items
    pivot = items[0]  # Опорное значение
    print(f"\nОпорное значение: {pivot}")
    left = [l for l in items if l < pivot]
    print(f"...Левая часть: {left}")
    mid = [m for m in items if m == pivot]
    print(f"....Центральная часть: {mid}")  # Список для борьбы с повторами
    right = [r for r in items if r > pivot]
    print(f".....Правая часть: {right}")

    print(f'Вызов сортировки для {left} и {right}')
    return quicksort_egoroff(left) + mid + quicksort_egoroff(right)


def quicksort(items, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1

    print(f"\n...Сортировка {items[left:right + 1]} ")
    print(f".......items: {items}")

    if right <= left:  # (1)
        # Если диапазон пустой или содержит один элемент значит отсортирован
        return  # Базовый случай

    i = left  # Исходное значение i соответствует левому концу диапазона (2)
    # Выбираем последнее значение в качестве опорного
    pivotValue = items[right]
    print(f".......pivot: {pivotValue}")

    # Производим итерацию вплоть до достижения опорного элемента, не включая его
    for j in range(left, right):
        # Если значение меньше опорного помещаем его в левую часть списка
        if items[j] <= pivotValue:
            # Меняем местами эти два значения
            items[i], items[j] = items[j], items[i]
            i += 1
    # Помещаем опорный элемент в левую часть списка 'items':
    items[i], items[right] = items[right], items[i]
    # Окончание процесса разбиения

    print(f"После замены: {items[left:right + 1]}")
    print(f".......Вызов: {items[left:i]} и {items[i + 1: right + 1]}")

    # Вызываем функцию для двух получ енных разделов
    quicksort(items, left, i - 1)
    quicksort(items, i + 1, right)


# my_list = [8, 7, 6, 3, 1, 2, 5, 4]
# my_list = [2, 3, 4, 5, 6, 1, 8, 9, 7]
my_list = [0, 7, 6, 3, 1, 2, 5, 4]
quicksort(my_list)
# quicksort_egoroff(my_list)
print(my_list)
