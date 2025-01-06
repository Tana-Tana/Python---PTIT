from itertools import *
xau = input()
res = permutations(xau)
for i in res: print(''.join(i))