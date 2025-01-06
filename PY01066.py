
def Check(xau):
    xauDao = xau[::-1]
    for i in range(len(xau)-1):
        if abs(ord(xau[i]) - ord(xau[i+1])) != abs(ord(xauDao[i]) - ord(xauDao[i+1])): return False
    return True

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        xau = input()
        if Check(xau): print("YES")
        else: print("NO")