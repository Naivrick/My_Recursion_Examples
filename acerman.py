import time



def ackerman(m,n, indentation = None):
    if indentation is None:
        indentation = 0
    print(f"{' ' * indentation} ({m}, {n})")
    if m == 0:
        # Базовый случай
        return n + 1
    elif m > 0 and n == 0:
        # Рекурсивный случай
        return ackerman(m-1, 1, indentation + 1)
    elif m > 0 and n > 0:
        # Рекурсивный случай
        return ackerman(m-1, ackerman(m, n - 1 ,indentation + 1), indentation + 1)
    


# print('Starting with m = 1, n = 1')
# ackerman(1,1)
# print('Starting with m = 2, n = 3')
# ackerman(2,3)
# print('Starting with m = 3, n = 4')
# ackerman(3,4)
ackerman(4,3)