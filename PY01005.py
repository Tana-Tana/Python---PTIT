n = input()
cnt4 = 0
cnt7 = 0
for i in range(0, len(n)):
    if n[i] == '4':
        cnt4 += 1
    else:
        if n[i] == '7':
            cnt7 += 1
res = round(cnt4+cnt7, 0)

if res == 4 or res == 7:
    print("YES")
else:
    print("NO")
