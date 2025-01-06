def dec_to_base_b(N,b):
    if N == 0: return 0
    res = ""
    while N != 0:
        if ( N%b > 9):
            res = chr( ord('A') +  N%b - 10) + res
        else : 
            res = str(N%b) + res
        N//=b
    return res

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        N,b = map(int, input().split())

        # Tinh toan
        print(dec_to_base_b(N,b))