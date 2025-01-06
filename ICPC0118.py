list_cung = ['0', 'Ma Ket', 'Bao Binh','Song Ngu', 'Bach Duong', 'Kim Nguu','Song Tu','Cu Giai','Su Tu','Xu Nu','Thien Binh','Thien Yet','Nhan Ma']

test = int(input())
while test > 0:
    test -= 1
    ngay,thang = map(int,input().split())
    if thang == 1 or thang == 4:
        if ngay > 19: print(list_cung[thang+1])
        else: print(list_cung[thang])
    elif thang == 2:
        if ngay > 18: print(list_cung[thang+1])
        else: print(list_cung[thang])
    elif thang == 3 or thang == 5 or thang == 6:
        if ngay > 20: print(list_cung[thang+1])
        else: print(list_cung[thang])
    elif thang == 7 or thang == 8 or thang == 9 or thang == 10 or thang == 11:
        if ngay > 22: print(list_cung[thang+1])
        else: print(list_cung[thang])
    elif thang == 12:
        if ngay > 21: print(list_cung[1])
        else: print(list_cung[thang])