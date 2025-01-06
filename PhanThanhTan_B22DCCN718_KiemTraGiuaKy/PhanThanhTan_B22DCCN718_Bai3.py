s = []
mp = dict()
mp['a'] = 'e'
mp['e'] = 'ai'
mp['i'] = 'aeuo'
mp['o'] = 'ui'
mp['u'] = 'a'
cnt = 0


def Try(idx):
    global n
    if idx == n:
        global cnt
        cnt += 1
    if idx == 0:
        for c in 'aeiou':
            s.append(c)
            Try(idx + 1)
            s.pop()
    elif idx < n:
        for c in mp[s[-1]]:
            s.append(c)
            Try(idx + 1)
            s.pop()


n = int(input())
Try(0)
print(cnt)
