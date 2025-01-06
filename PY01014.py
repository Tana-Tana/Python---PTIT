
if __name__ == "__main__":
    a,k,n = map(int, input().split())
    b = -1 
    if a >= n: print(b)
    else :
        b = (a//k + 1)*k - a
        check  = 1
        while b <= n-a:
            print(b, end = ' ')
            check = 0
            b += k
        if check == 1: print(-1)
    

    
        