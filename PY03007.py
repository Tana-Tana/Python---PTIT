# WA
xau = ''
while True: 
    try : xau += input()
    except EOFError : break
xau = xau.split()
res = ''
for i in xau:
    res += (i + ' ')
    if (i[len(i)-1] == '.') or (i[len(i)-1] == '?') or (i[len(i)-1] == '!'):
        res = list(res.lower().capitalize().split())
        
        # check xau in ra co it nhat 1 ki tu so hoac chu cai
        cnt = 0
        for i in res:
            if cnt != 0: break
            for j in i:
                if cnt != 0: break
                if (j.isdigit() == True) or (j.isalpha() == True): cnt+=1
        if cnt!=0:
            for i in range(len(res)):
                for j in range(len(res[i])):
                    if (res[i][j] == '.') or (res[i][j] =='?') or (res[i][j] == '!'): continue
                    else: print(res[i][j],end = '')
                if i!= len(res) - 1: print(' ',end = '')
            print()
        res = ''
if res != ' ':
    res = list(res.lower().capitalize().split())
    # check xau in ra co it nhat 1 ki tu so hoac chu cai
    cnt = 0
    for i in res:
        if cnt != 0: break
        for j in i:
            if cnt != 0: break
            if (j.isdigit() == True) or (j.isalpha() == True): cnt+=1
    if cnt!=0:
        for i in range(len(res)):
            for j in range(len(res[i])):
                if (res[i][j] == '.') or (res[i][j] =='?') or (res[i][j] == '!'): continue
                else: print(res[i][j],end = '')
            if i!= len(res) - 1: print(' ',end = '')
        print()