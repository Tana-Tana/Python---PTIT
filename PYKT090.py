with open('CONTACT.in', 'r') as file:
    _list = file.readlines()
list_res = []
for  i in _list:
    res = i.split('\n')
    for z in res:
        if z!='': list_res.append(z.lower())
dict_res = {}
for i in list_res:
    if not (i in dict_res): dict_res[i] = 1
    else: continue
dict_res = dict(sorted(dict_res.items(), key = lambda x : x[0]))
for i in dict_res: print(i)