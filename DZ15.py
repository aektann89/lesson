from math import *

x1 = float(input('Введите x1:'))
y1 = float(input('Введите y1:'))
x2 = float(input('Введите x2:'))
y2 = float(input('Введите y2:'))


def distance(x1, y1, x2, y2):
    c = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return c


c = distance(x1, y1, x2, y2)
print(c)
