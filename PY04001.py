from math import *
from decimal import *
class Point:
    x,y = None,None
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self, other):
        a = (self.x - other.x) ** 2
        b = (self.y - other.y) ** 2
        return f"{'{:.4f}'.format(sqrt(a+b))}"

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1