def tinh_tich_chu_so(number):
    sum = 1
    while number !=0:
        sum *= (number%10)
        number//=10
    return sum

#main
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr = sorted(arr, key = lambda x : (tinh_tich_chu_so(x), x))
    for i in arr: 
        print(i,end = ' ')
    print()