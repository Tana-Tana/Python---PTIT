if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        xau = input()
        #xu li
        sum = 0
        res = []
        for i in xau:
            if i.isdigit(): sum += int(i)
            else: res.append(i)
        res.sort()
        res = ''.join(res) + str(sum)
        print(res)
