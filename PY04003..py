from math import *
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def __str__(self):
        return f"{int(self.tu)}/{int(self.mau)}"
    
    def toiGian(self):
        _gcd = gcd(self.tu, self.mau)
        self.tu /= _gcd
        self.mau /= _gcd
#main
a,b = map(int, input().split())
phanSo = PhanSo(a,b)
phanSo.toiGian()
print(phanSo)