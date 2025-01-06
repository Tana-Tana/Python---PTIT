test = int(input())
while test > 0:
    test -= 1
    n,d = map(int, input().split())
    arr = list(map(int, input().split()))
    so_lan_xoay = d%n
    arr = arr[so_lan_xoay:] + arr[:so_lan_xoay]
    for i in arr: print(i,end = ' ')
    print()