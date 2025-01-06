def Check(number):
    number_start = list(number)[:2]
    number_end = list(number)[len(number)-2:]
    # print(number_start,number_end)
    if number_start == number_end: return True
    else: return False

if __name__ == '__main__':
    test = int(input())
    while test > 0:
        test -= 1
        number = input()
        if Check(number) == True: print("YES")
        else : print("NO")