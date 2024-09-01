test = int(input())
for z in range(0, test):
    str_number = input()
    lenth = len(str_number)
    res = ""
    if lenth == 1:
        print(str_number)
    else:
        for i in range(lenth - 1, 0, -1):
            k = int(str_number[i])
            if(k < 5):
                res += '0'
            else:
                res += '0'
                j = i - 1
                xau = ""
                if str_number[j] == '0':
                    xau = str_number[0: i-1] + \
                        "1" + str_number[i+1: lenth]

                if str_number[j] == '1':
                    xau = str_number[0: i-1] + \
                        "2" + str_number[i+1: lenth]

                if str_number[j] == '2':
                    xau = str_number[0: i-1] + \
                        "3" + str_number[i+1: lenth]

                if str_number[j] == '3':
                    xau = str_number[0: i-1] + \
                        "4" + str_number[i+1: lenth]

                if str_number[j] == '4':
                    xau = str_number[0: i-1] + \
                        "5" + str_number[i+1: lenth]

                if str_number[j] == '5':
                    xau = str_number[0: i-1] + \
                        "6" + str_number[i+1: lenth]

                if str_number[j] == '6':
                    xau = str_number[0: i-1] + \
                        "7" + str_number[i+1: lenth]

                if str_number[j] == '7':
                    xau = str_number[0: i-1] + \
                        "8" + str_number[i+1: lenth]

                if str_number[j] == '8':
                    xau = str_number[0: i-1] + \
                        "9" + str_number[i+1: lenth]
                else:
                    if str_number[j] == '9':
                        xau = xau = str_number[0: i-1] + \
                            "9" + str_number[i+1: lenth]
                str_number = xau

        if str_number[0] != '9':
            res = str_number[0] + res
        else:
            res = "10" + res
        print(res)
