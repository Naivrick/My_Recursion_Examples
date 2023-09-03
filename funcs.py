def sumSeriesIteration(number):
    return sum(range(number + 1))

# print(sumSeriesIteration(3)) # 6
# print(sumSeriesIteration(2)) # 3
# print(sumSeriesIteration(4)) # 10

def sumSeries_recursion(number):
    if number == 0:
        return 0
    return number + sumSeries_recursion(number - 1)

# print(sumSeries_recursion(3)) # 6
# print(sumSeries_recursion(2)) # 3
# print(sumSeries_recursion(4)) # 10

def sumPowerOf2(number):
    res = 0
    for i in range(1,number+1):
        res = res + 2 ** i
    return res


# print(sumPowerOf2(1)) # 2
# print(sumPowerOf2(2)) # 6 
# print(sumPowerOf2(3)) # 14

def sumPowerOf2_recursion(number):
    if number == 1:
        return 2
    return 2 ** number + sumPowerOf2_recursion(number - 1)

# print(sumPowerOf2_recursion(1)) # 2
# print(sumPowerOf2_recursion(2)) # 6 
# print(sumPowerOf2_recursion(3)) # 14 