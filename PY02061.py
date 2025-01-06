test = int(input())
while test > 0:
    test -= 1
    n,m = map(int, input().split())
    res = []
    for i in range(n):
        a = [int(i) for i in input().split()]
        res.append(a)

    kernel = []
    for i in range(3):
        a = [int(i) for i in input().split()]
        kernel.append(a)

    # duyet mang 2 chieu
    sum = 0
    for i in range(n - 2):
        a = res[i:i+3]
        for j in range(m-2):
            b = []
            for z in a:
                c = z[j:j+3]
                b.append(c)
            # tinh sum
            for z in range(len(b)):
                for k in range(len(b[z])):
                    sum += (b[z][k] * kernel[z][k])
    print(sum)