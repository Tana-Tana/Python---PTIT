def TinhToanSoNam(tienGoc, laiMoiNam, MucTienCanDatDuoc):
    soNam = 0
    while tienGoc < MucTienCanDatDuoc:
        tienGoc = tienGoc + tienGoc*laiMoiNam/100
        soNam+=1
    return soNam
    

if __name__ == '__main__':
    test = int(input())
    while test > 0:
        test -= 1
        n,x,m = map(float, input().split())
        print(TinhToanSoNam(n,x,m))
