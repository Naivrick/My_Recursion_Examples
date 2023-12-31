import sys


img = [
list('___________________¶¶¶¶¶________________________'),
list('__________________¶¶¶¶¶¶________________________'),
list('________________¶¶¶¶¶¶¶_________________________'),
list('_______________¶¶¶¶¶¶¶¶_________________________'),
list('_______________¶¶¶¶¶¶¶¶_________________________'),
list('______________¶¶¶¶¶¶¶¶¶¶________________________'),
list('______________¶¶¶¶¶¶¶¶¶¶________________________'),
list('______________¶¶¶¶¶¶¶¶¶¶¶______________¶¶¶______'),
list('______________¶¶¶¶¶¶¶¶¶¶¶¶___________¶¶¶¶_______'),
list('_______¶______¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶¶¶_______'),
list('_______¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶_______'),
list('_______¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶_______'),
list('_______¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶_______'),
list('_______¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______'),
list('_______¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______'),
list('______¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____'),
list('_____¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____'),
list('___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___'),
list('__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__'),
list('__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__'),
list('_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_'),
list('_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶______¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_'),
list('_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_'),
list('_¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶__'),
list('_¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶____¶¶¶¶¶¶¶¶¶¶¶___'),
list('__¶¶¶¶¶¶¶¶¶¶¶¶_____________________¶¶¶¶¶¶¶¶¶____'),
list('____¶¶¶¶¶¶¶¶¶¶_____________________¶¶¶¶¶¶¶¶_____'),
list('______¶¶¶¶¶¶¶¶_____________________¶¶¶¶¶¶_______'),
list('_________¶¶¶¶¶¶___________________¶¶¶¶__________'),
list('_____________¶¶¶¶¶______________¶_______________'),
]

HEIGHT = len(img)
WIDTH = len(img[0])


def floodFill(image, x,y,newChar, oldChar=None):
    if oldChar  == None:
        # в oldChar по умолчанию сохраняется символ в точке с координатами x,y  
        oldChar = image[x][y]
    if oldChar == newChar or image[y][x] != oldChar:
        #Базовый случай
        return
    
    image[y][x] = newChar # Изменение символа

    if y + 1 < HEIGHT and image[y+1][x] == oldChar:
        floodFill(image, x, y + 1, newChar, oldChar)
    
    if y - 1 >= 0 and image[y - 1][x] == oldChar:
        floodFill(image, x, y - 1, newChar, oldChar)
    
    if x + 1 < WIDTH and image[y][x + 1] == oldChar:
        floodFill(image, x + 1, y, newChar, oldChar)
    
    if x - 1 >= 0 and image[y][x - 1] == oldChar:
        floodFill(image, x - 1, y, newChar, oldChar)
    return

def printImage(image):
    for y in range(HEIGHT):
        # Вывод каждой строки
        for x in range(WIDTH):
            # Вывод каждого столбца на экран
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')

printImage(img)
floodFill(img,25,17,' ')
floodFill(img,0,0,' ')
printImage(img)
    

