#ARCHIVE

def recursive(value):
    print(value)
    if value < 4:
        recursive(value + 1)
    print(value)

# recursive(1)

def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n-1)


# print(factorial(6))



F = \
{
    'C' : 
    {
        'Python' : ['main.py', 'python.ini'],
        'Temp':'temp',
        'Program Files': ['README.txt','text.txt','image.png', 'virus.exe'],
        'AppData' : [],
        'Windows95' : 
        {
            'System16': ['hosts','lib.dll','winrar','YandexAgent'],
            'Uzver':['por.wtf','dot.net']
        } ,
    }
}


def get_files(path, depth=0):
    for f in path:
        print(' '*depth, f)
        if type(path[f])== dict:
            get_files(path[f], depth+5)
        else:
            print(' '*(depth+5), ' '.join(path[f]))
                  
get_files(F)