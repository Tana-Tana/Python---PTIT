def ChuyenDoi(xau):
    for i in range(0,len(xau),2) :
        for j in range(int(xau[i+1])):
            print(xau[i],end = '')

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = input()
        ChuyenDoi(number)
        print()
