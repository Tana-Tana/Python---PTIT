from math import *
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def tong(self, other):
        mau_chung = self.mau * other.mau
        tu_chung = (mau_chung// self. mau) * self.tu + (mau_chung//other.mau) * other.tu
        _gcd = gcd(tu_chung, mau_chung)
        tu_chung//= _gcd
        mau_chung//= _gcd
        return f"{tu_chung}/{mau_chung}"
#main
a,b,c,d = map(int, input().split())
x = PhanSo(a,b)
print(x.tong(PhanSo(c,d)))