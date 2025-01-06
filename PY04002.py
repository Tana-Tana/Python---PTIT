class Rectangle:
    def __init__(self, chieu_dai, chieu_rong, mau_sac):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
        self.mau_sac = mau_sac
    
    def perimeter(self):
        return (self.chieu_dai + self.chieu_rong)*2
    
    def area(self):
        return self.chieu_dai * self.chieu_rong
    
    def color(self):
        return self.mau_sac.lower().title()
#main
arr = input().split()
if  int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")
