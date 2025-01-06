class sinh_vien:
    ten = None
    so_bai_lam_dung = None
    so_luot_sub = None

    def __init__(self, ten, so_bai_lam_dung, so_luot_sub):
        self.ten = ten
        self.so_bai_lam_dung = so_bai_lam_dung
        self.so_luot_sub = so_luot_sub
    
    def __lt__(self, other):
        if self.so_bai_lam_dung == other.so_bai_lam_dung:
            if self.so_luot_sub == other.so_luot_sub:
                return self.ten < other.ten
            else: return self.so_luot_sub < other.so_luot_sub
        else: return self.so_bai_lam_dung == other.so_bai_lam_dung

    def __str__(self):
        return f"{self.ten} {self.so_bai_lam_dung} {self.so_luot_sub}"

if __name__ == '__main__':
    test = int(input())
    arr = []
    while test > 0:
        test -= 1
        a = input()
        b,c = map(int, input().split())
        sv = sinh_vien(a,b,c)
        arr.append(sv)
    arr = sorted(arr)
    for sv in arr:
        print(sv)