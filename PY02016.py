test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    arr = [int(i) for i in input().split()]
    dict_n = {}
    for i in arr:
        if not (i in dict_n): dict_n[i] = 1
        else: dict_n[i] +=1
    dict_n = dict(sorted(dict_n.items(), key = lambda x : (-x[1],x[0])))
    for key, value in dict_n.items():
        if value > (n//2): print(key); break
        else:
            print("NO")
            break