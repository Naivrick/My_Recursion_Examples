import os 
#import time

MAZE = '''
#######################################################################
#S#                 #       # #   #     #         #     #   #         #
# ##### ######### # ### ### # # # # ### # # ##### # ### # # ##### # ###
# #   #     #     #     #   # # #   # #   # #       # # # #     # #   #
# # # ##### # ########### ### # ##### ##### ######### # # ##### ### # #
#   #     # # #     #   #   #   #         #       #   #   #   #   # # #
######### # # # ##### # ### # ########### ####### # # ##### ##### ### #
#       # # # #     # #     # #   #   #   #     # # #   #         #   #
# # ##### # # ### # # ####### # # # # # # # ##### ### ### ######### # #
# # #   # # #   # # #     #     #   #   #   #   #   #     #         # #
### # # # # ### # # ##### ####### ########### # ### # ##### ##### ### #
#   # #   # #   # #     #   #     #       #   #     # #     #     #   #
# ### ####### ##### ### ### ####### ##### # ######### ### ### ##### ###
#   #         #     #     #       #   # #   # #     #   # #   # #   # #
### ########### # ####### ####### ### # ##### # # ##### # # ### # ### #
#   #   #       # #     #   #   #     #       # # #     # # #   # #   #
# ### # # ####### # ### ##### # ####### ### ### # # ####### # # # ### #
#     #         #     #       #           #     #           # #      E#
#######################################################################
'''.split('\n')


EMPTY = ' '
START = 'S'
EXIT = 'E'
PATH = '.'

# Получаем значение высоты и ширины лабиринта
HEIGHT = len(MAZE)
WIDTH = 0
for row in MAZE: # Задаем для WIDTH значение самой широкой строки
    if len(row) > WIDTH:
        WIDTH = len(row)

# Превращаем каждую строку в лабиринте в список шириной WIDTH:
for i in range(len(MAZE)):
    MAZE[i] = list(MAZE[i])
    if len(MAZE[i]) != WIDTH:
        MAZE[i] = [EMPTY] * WIDTH # Делаем эту сроку пустой

def printMaze(maze):
    for y in range(HEIGHT):
        #  Выводим на экран каждую строку
        for x in range(WIDTH):
            #  Выводим на экран каждый столбец в этой строке
            print(maze[y][x], end='')

        print() # Добавляем в конце переход на новую строку
    print()


def findStart(maze):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if MAZE[y][x] == START:
                return(x,y) #  Возвращаем коры входа в лабиринт

def solveMaze(maze, x = None, y =None, visited = None):
    if x == None or y == None:
        x, y = findStart(maze)
        maze[y][x] = EMPTY # Избавляемся от буквы 'S' в лабиринте
    if visited == None:
        visited = [] #  Создаём список посещенных точек
    
    if maze[y][x] == EXIT:
        return True # Выход найден, возвращаем True
    
    maze[y][x] = PATH # Отмечаем пусть в лабиринте
    visited.append(f"{str(x)},{str(y)}")
    
    printMaze(maze) # Для просмотра каждого шага

    # Проверяем северную соседнею точку:
    if y + 1 < HEIGHT and maze[y+1][x] in (EMPTY, EXIT) and f"{str(x)},{str(y + 1)}" not in visited:
        # Рекурсивный случай
        if solveMaze(maze, x,y + 1, visited):
            return True # базовый случай
        
    # Проверяем южную соседнею точку:
    if y - 1 >= 0 and maze[y - 1][x] in (EMPTY, EXIT) and f"{str(x)},{str(y - 1)}" not in visited:
        # Рекурсивный случай
        if solveMaze(maze, x,y - 1, visited):
            return True # базовый случай
        
    # Проверяем восточную соседнею точку:
    if x + 1 < WIDTH and maze[y][x + 1] in (EMPTY, EXIT) and f"{str(x + 1)},{str(y)}" not in visited:
        # Рекурсивный случай
        if solveMaze(maze, x + 1,y, visited):
            return True # базовый случай
        
    # Проверяем западную соседнею точку:
    if x - 1 < WIDTH and maze[y][x - 1] in (EMPTY, EXIT) and f"{str(x - 1)},{str(y)}" not in visited:
        # Рекурсивный случай
        if solveMaze(maze, x - 1,y, visited):
            return True # базовый случай
    
    maze[y][x] = EMPTY # Заменяем пробелы точками
    
    printMaze(maze) # Для просмотра каждого шага назад

    return False # Базовый случай

printMaze(MAZE)
solveMaze(MAZE)
printMaze(MAZE)