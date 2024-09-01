n = input()
cnt1 = 0
cnt2 = 0
for i in range(0, len(n)):
    if n[i] >= 'a' and n[i] <= 'z':
        cnt1 += 1
    else:
        if n[i] >= 'A' and n[i] <= 'Z':
            cnt2 += 1

if(cnt1 >= cnt2):
    print(n.lower())
else:
    print(n.upper())
