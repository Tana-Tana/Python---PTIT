def KT(number):
    if(number[len(number)-2:] == "86"): return True
    return False

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        number = input()
        if KT(number) == True: print("YES")
        else: print("NO")