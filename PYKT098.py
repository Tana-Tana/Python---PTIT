#doc file
with open('DATA.in', 'r') as file:
    xau = file.readlines()
    # print(xau)
res = []
for i in xau:
    a = [str(j) for j in i.split()]
    for z in a: res.append(z)
a = []
for i in res:
    if i.isdigit():
        if -2**31 - 1 <= int(i) <= 2**31 - 1: continue
        else: a.append(i)
    else: a.append(i)
a = sorted(a)
print(' '.join(a)) 