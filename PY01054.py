if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = input()
        res = 1
        for i in number:
            if int(i) == 0: continue
            res*=int(i)
        print(res)