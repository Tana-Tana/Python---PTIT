import math
m, n = map(int, input().split())
ans = 0
anssqr = 0
ok = 1


def calcSqr(a):
    st = []
    l = [0] * n
    r = [0] * n
    for i in range(n):
        while len(st) > 0 and a[i] <= a[st[-1]]:
            st.pop()
        if len(st) == 0:
            l[i] = 0
        else:
            l[i] = st[-1] + 1
        st.append(i)
    st = []
    for i in range(n-1, -1, -1):
        while len(st) > 0 and a[i] <= a[st[-1]]:
            st.pop()
        if len(st) == 0:
            r[i] = n - 1
        else:
            r[i] = st[-1] - 1
        st.append(i)
    tmp = 0
    for i in range(n):
        if a[i] <= (r[i] - l[i] + 1):
            tmp = max(tmp, a[i]*a[i])
    return tmp


def calc(a):
    st = []
    l = [0] * n
    r = [0] * n
    for i in range(n):
        while len(st) > 0 and a[i] <= a[st[-1]]:
            st.pop()
        if len(st) == 0:
            l[i] = 0
        else:
            l[i] = st[-1] + 1
        st.append(i)
    st = []
    for i in range(n-1, -1, -1):
        while len(st) > 0 and a[i] <= a[st[-1]]:
            st.pop()
        if len(st) == 0:
            r[i] = n - 1
        else:
            r[i] = st[-1] - 1
        st.append(i)
    tmp = 0
    for i in range(n):
        tmp = max(tmp, a[i] * (r[i] - l[i] + 1))
    return tmp


a = [0] * m * n

b = [[0 for _ in range(n)] for _ in range(m)]
a = [[int(x) for x in input().split()] for _ in range(m)]
st = []
for i in range(m):
    if i == 0:
        for j in range(n):
            b[i][j] = a[i][j]
    else:
        for j in range(n):
            if a[i][j] != 0:
                b[i][j] = a[i][j] + b[i-1][j]
            else:
                b[i][j] = 0
for i in range(m):
    anssqr = max(anssqr, calcSqr(b[i]))
    ans = max(ans, calc(b[i]))
print("OUTPUT_1 =", anssqr, sep=" ")
print("OUTPUT_2 =", ans, sep=" ")
