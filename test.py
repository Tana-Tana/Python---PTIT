def CheckCSC(test):
    res = []
    for case in test:
        n, arr = case
        arr.sort()  # sap xep mang tang dan
        check= True
        d = arr[1] - arr[0]  # cong sai
        for i in range(1, n - 1):
            if arr[i + 1] - arr[i] != d:  # kiem tra cong sai
                check = False
                break
        res.append("YES" if check else "no")
    return res

# main
t = int(input())  # test
test = []
for _ in range(t):
    n = int(input())  
    arr = list(map(int, input().split()))
    test.append((n, arr))
results = CheckCSC(test)
print("\n".join(results))
