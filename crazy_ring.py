import math
from operator import itemgetter


def calculatedistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


n1, m1 = itemgetter(0, 1)(list(int(n) for n in input().split(" ")))
n2, m2 = itemgetter(0, 1)(list(int(n) for n in input().split(" ")))
n3, m3 = itemgetter(0, 1)(list(int(n) for n in input().split(" ")))

a = calculatedistance(n1, m1, n2, m2)
b = calculatedistance(n2, m2, n3, m3)
c = calculatedistance(n3, m3, n1, m1)
s = (a + b + c) / 2

if a + b >= c and b + c >= a and a + c >= b:
    R = a * b * c / math.sqrt((a + b + c) * (a + b - c) * (a + c - b) * (b + c - a))
    r = math.sqrt(((s - a) * (s - b) * (s - c)) / s)
    ring = math.pi * ((R ** 2) - (r ** 2))
    print('%.2f' % ring)
else:
    print("not possible")
