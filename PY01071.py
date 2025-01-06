def Check(xau):
    xau = xau.lower()
    if xau[len(xau)-3:] != ".py": return False
    for i in xau:
        if (i == '_') or (i=='.') or ('a' <= i <= 'z'): continue
        else: return False
    return True

# main
xau = input()
if Check(xau): print("yes")
else: print("no")