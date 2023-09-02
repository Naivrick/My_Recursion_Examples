# %%

def recurse_find_even(nums: list,result = []): #  Функция должна возвращает список чётных чисел
    
    
    if not nums: # Если список пустой
        return # выходим
    else:
        first_element = nums[0]
        if first_element % 2 == 0:
            result.append(first_element)
        recurse_find_even(nums[1:])
        return result
    
print(recurse_find_even([1,2,3,4,5,6,7,8,9,10]))

# %%
# 4 пункт 

def a():
    print("функция а() вызвана")
    b()
    print("функция a() продолжает работу")

def b():
    print("функция b() вызвана")
    c()
    print("функция b() продолжает работу")

def c():
    print("функция c() вызвана")
    print("функция c() продолжает работу")

a()

# %% [markdown]
# Стек

# %%
# Демонстрация стека на примере list
stack = []
 
# append() как push
stack.append('J')
stack.append('Q')
stack.pop()
stack.append('K')
stack.pop()
print(stack)

# print("Текущий 'стек'")
# print(stack)
 
# # pop() как pop
# print('\nЭлементы покидают стек:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
 
# print('\nПустой стек:')
# print(stack)
 

# %%
def shortestWithBaseCase(makeRecursiveCall): 
  print(f'Короткий тест с базовым случаем {makeRecursiveCall} вызван.')
  if not makeRecursiveCall:
    # БАЗОВЫЙ СЛУЧАЙ
    print('Возвращение из базового случая.')
  else:
    # РЕКУРСИВНЫЙ СЛУЧАЙ
    print("Вызов рекурсивной функции:")
    shortestWithBaseCase(False)
    print('Возвращение из рекурсивного случая.')
    return

print("Вызываем функцию с False")
shortestWithBaseCase(False)
print()
print("Вызываем функцию с True")
shortestWithBaseCase(True)

# %%
def countDownAndUp(number):
    print(f"Текущие число: {number}")
    if number == 0:
        #БАЗОВЫЙ СЛУЧАЙ
        print(f"Дошли до базового случая")
        return
    else:
        #РЕКУРСИВНЫЙ СЛУЧАЙ
        countDownAndUp(number - 1)
        print(f"Возращение {number}")
        return
    
countDownAndUp(3)

# %%
def factorial(number):
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product

print(factorial(10))

# %%
def factorial(number):
    if number == 1:
        # БАЗОВЫЙ СЛУЧАЙ
        return 1
    else:
        # РЕКУРСИВНЫЙ СЛУЧАЙ
        return number * factorial(number - 1)
    
print(factorial(5))

# %%
def fibonacci(nthNumber):
    a,b = 1,1
    print(f"a = {a}, b = {b}")
    for i in range(1, nthNumber):
        a,b = b, a + b # Получение следующего числа Фибоначчи
        print(f"a = {a}, b = {b}")
    return a

print(fibonacci(10))

# %%
def fibonacci(nthNumber):
    print(f"fibonacci {nthNumber} called")
    if nthNumber == 1 or nthNumber == 2:
        #Базовый случай
        print(f"Call ro fibonacci {nthNumber} returning 1")
        return 1
    else:
        #Рекурсивный случай
        print(f"Calling fibonacci({nthNumber - 1}) and fibonacci({nthNumber - 2})")
        result = fibonacci(nthNumber - 1) + fibonacci(nthNumber - 2)
        print(f"Call to fibonacci {nthNumber} returning {result}")
        return result

print(fibonacci(10))

# %%
callStack = [] # Явный стек вызовов, содержащий кадры
callStack.append({'returnAddr' : 'start', 'number' : 5})
# Вызов функции factorial()
returnValue = None

while len(callStack) > 0:
    # Тело "Функции factorial():"
    number = callStack[-1]['number'] # Задание числового параметра
    returnAddr = callStack[-1]['returnAddr']

    if returnAddr == 'start':
        if number == 1:
            # Базовый случай
            returnValue = 1
            callStack.pop() # Возврат из функции
            continue
        else:
            # Рекурсивный случай
            callStack[-1]['returnAddr'] = 'after recursive call'
            # Вызов функции factorial():
            callStack.append({'returnAddr' : 'start', 'number' : number - 1})
            continue
    elif returnAddr == 'after recursive call':
        returnValue = number * returnValue
        callStack.pop() # Возврат из вызова функции
        continue
    
print(returnValue)

# %%
print("Цикл: ")
i = 0
while i <= 5:
    print(i, 'Hello world')
    i += 1

print('Рекурсия:')
def hello(i = 0):
    print(i, 'Hello world')
    if i < 5:
        hello(i+1)
    else:
        return

hello()

# %%
# needle (Игла) , haystack (стог сена)

def findSubstringIterative(needle, haystack):
    i = 0
    while i < len(haystack):
        if haystack[i: i + len(needle)] == needle:
            return i # Игла найдена
        i += 1
    return -1 # Игла не найдена

def findSubstringRecursive(needle, haystack, i=0):
    if i > len(haystack):
        return -1 #Базовый случай (игла не найдена)
    if haystack[i:i+len(needle)] == needle:
        return i # Базовый случай (игла найдена)
    else:
        # рек случай
        return findSubstringRecursive(needle, haystack, i + 1)

print(findSubstringRecursive('cat', 'my cat bad'))
print(findSubstringIterative('cat', 'my cat bad'))

# %%
%%timeit
def exponentByIteration(a,n):
    res = 1
    for i in range(n):
        res *= a
    return res

print(exponentByIteration(3,6))
print(exponentByIteration(10,3))
print(exponentByIteration(17,30))
print(exponentByIteration(3,1000))

# %%
%%timeit
def exponentByRecursion(a,n):
    if n == 1:
        # базовый случай
        return a
    elif n % 2 == 0:
        # рекурсивный случай
        result = exponentByRecursion(a,n // 2)
        return result * result
    elif n % 2 == 1:
        # рекурсивный случай
        result = exponentByRecursion(a,n // 2)
        return result * result * a

print(exponentByRecursion(3,6))
print(exponentByRecursion(10,3))
print(exponentByRecursion(17,30))
print(exponentByRecursion(3,1000))

# %%



