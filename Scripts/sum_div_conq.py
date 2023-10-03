def sumDivConq(numbers: list):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        mid = len(numbers) // 2
        leftHalfSum = sumDivConq(numbers[0:mid])
        rightHalfSum = sumDivConq(numbers[mid: len(numbers) + 1])
        return leftHalfSum + rightHalfSum


print(sumDivConq([2, 2, 2, 2]))
