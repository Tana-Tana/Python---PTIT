def check(number):
    cnt4 = 0
    cnt7 = 0
    while number!=0:
        if number%10 == 4: cnt4 += 1
        if number%10 == 7: cnt7 += 1
        number//=10
    
    if (cnt4 + cnt7 == 4) or (cnt4 + cnt7 == 7): return True
    return False

if __name__ == '__main__':
    number = int(input())
    if check(number) == True: print("YES")
    else: print("NO")