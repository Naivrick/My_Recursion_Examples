def binarySearch(needle, haystack, left=None, right=None):

    if left is None and right is None:
        left = 0
        right = len(haystack) - 1
    print(f"Поиск в {haystack[left:right + 1]}")

    if left > right:
        # Базовый случай
        return None  # Значение needle отсутствует

    mid = (left+right) // 2

    if needle == haystack[mid]:
        # Базовый случай
        return mid
    elif needle < haystack[mid]:
        return binarySearch(needle, haystack, left, mid - 1)
    elif needle > haystack[mid]:
        return binarySearch(needle, haystack, mid + 1, right)


print(binarySearch(29, [1, 4, 5, 6, 7, 8, 9, 14,
      15, 17, 18, 19, 22, 26, 28, 29, 36, 57]))
