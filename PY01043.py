def Check(number):
    l = 0
    r = len(number)-1
    if len(number)%2==1: return False
    while l<= r:
        if (number[l]!=number[r]): return False
        if(int(number[l]) % 2 == 1) or (int(number[r])%2 == 1): return False
        l+=1
        r-=1
    return True


if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        n = int(input())
        for i in range(22, n,22):
            if Check(str(i)) == True: print(i, end = ' ')
        print()