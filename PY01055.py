def Check(number):
    if len(number)%2==0: return False
    
    if int(number[0]) == int(number[1]): return False
    for i in range(len(number)):
        if (i%2==0) and (int(number[0]) != int(number[i])): return False
    return True 

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = input()
        if Check(number): print("YES")
        else: print("NO")