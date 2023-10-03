"""Алгоритм сортировка слиянием

подход "разделение - слияние"

Разработана математиком Джон фон Нейман в 1945 году.
"""
import math


def mergeSort(items):
    print(f'.....mergeSort() called on: {items}')

    # !БАЗОВЫЙ СЛУЧАЙ
    # Пустой список или список из 1 элемента
    if len(items) <= 1:
        return items  # ?(1)

    # !РЕКУРСИВНЫЙ СЛУЧАЙ
    # Передаём левую и правую часть списка

    # Округляем в меньшую сторону, если не делиться на пополам
    iMiddle = math.floor(len(items)/2)  # ?(2)
    print(f'................Split into: {items[:iMiddle]} & {items[iMiddle:]}')

    left = mergeSort(items[:iMiddle])  # ?(3)
    right = mergeSort(items[iMiddle:])

    # !БАЗОВЫЙ СЛУЧАЙ
    # возврат объединенных, отсортированных данных:
    # на этом этапе левая и правая половина должны быть отсортированы
    # Мы можем объединить их в один отсортированный список.

    sortedResult = []
    iLeft = 0
    iRight = 0
    while (len(sortedResult) < len(items)):
        if left[iLeft] < right[iRight]:  # ?(4)
            sortedResult.append(left[iLeft])
            iLeft += 1
        else:
            sortedResult.append(right[iRight])
            iRight += 1
        # Если один из указателей достиг конца своего списка,
        # помещаем часть другого списка в sortedResult
        if iLeft == len(left):
            sortedResult.extend(right[iRight:])
            break
        elif iRight == len(right):
            sortedResult.extend(left[iLeft:])
            break
    print(f'The two halves merged into: {sortedResult}')

    return sortedResult  # Возврат отсортированной версии списка items


myList = [2, 9, 8, 5, 3, 4, 7, 6]
sortList = mergeSort(myList)
print(f"NoSort: {myList}")
print(f"  Sort: {sortList}")
