import sys

# Создание стержней A,B,C конец списка соответствует вершине стержня
TOTAL_DISK = 20

# Заполнение стержня A Кольцами
TOWERS = {'A' : list(reversed(range(1,TOTAL_DISK+1))),
          'B' : [],
          'C' : [],
          }

def printDisk(diskNum):
    # Вывод на экран одного кольца шириной diskNum
    emptySpace = ' ' * (TOTAL_DISK - diskNum)
    if diskNum == 0:
        # Рисование пустого стержня
        sys.stdout.write(emptySpace + '||' + emptySpace)
    else:
        # Рисование кольца
        diskSpace = '@' * diskNum
        diskNumLabel = str(diskNum).rjust(2, ' ')
        sys.stdout.write(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace)

def printTowers():
    #Вывод га экран всех трёх башен
    for level in range(TOTAL_DISK, -1 , -1):
        for tower in (TOWERS['A'], TOWERS["B"], TOWERS['C']):
            if level >= len(tower):
                printDisk(0)
            else:
                printDisk(tower[level])
        sys.stdout.write('\n')
    #Вывод на экран меток A,B,C
    empty_space = ' ' * (TOTAL_DISK)
    #print(f"{empty_space} A{empty_space}{empty_space} B{empty_space}{empty_space} C")
    print('%s A%s%s B%s%s C\n' % (empty_space,empty_space,empty_space,empty_space,empty_space))


def moveOneDisk(startTower, endTower):
    # Перемещение верхнего кольца с начального стержня на конечный
    disk = TOWERS[startTower].pop()
    TOWERS[endTower].append(disk)

def solve(numberOfDisks, startTower, endTower, tempTower):
    # Перемещение верхних numberOfDisks колец с начального стержня на конечный 
    if numberOfDisks == 1:
        # Базовый случай
        moveOneDisk(startTower, endTower)
        printTowers()
        return
    else:
        # Рекурсивный случай
        solve(numberOfDisks - 1, startTower, tempTower, endTower)
        moveOneDisk(startTower, endTower)
        printTowers()
        solve(numberOfDisks - 1, tempTower, endTower, startTower)
        return

# Решение
printTowers()
solve(TOTAL_DISK, "A", 'B', 'C')
