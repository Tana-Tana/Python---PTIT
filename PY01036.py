if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        number = int(input())
        tong = 0
        if number % 2 == 0:
            for i in range(2,number+1,2):
                tong += 1/i
        else :
            for i in range(1,number+1,2):
                tong += 1/i
        print('{:.6f}'.format(tong))