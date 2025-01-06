def CheckKC(xau):
    xauDao = xau[::-1]
    for i in range(1,len(xau),2):
        if abs(ord(xau[i]) - ord(xau[i-1])) != \
           abs(ord(xauDao[i]) - ord(xauDao[i-1])): return False
    
    return True

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        xau = list(input())
        if CheckKC(xau) == True: print("YES")
        else: print("NO")