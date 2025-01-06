def cd(number1, number2, a, b):
    for i in range(len(number1)):
        if number1[i] == chr(b + 48):
            number1[i] = chr(a+ 48)
    for i in range(len(number2)):
        if number2[i] == chr(b+ 48):
            number2[i] = chr(a+ 48)
    return int(''.join(number1)) + int(''.join(number2))


#main
test = int(input())
while test > 0:
    test -= 1
    a,b = map(int, input().split())
    if a < b: a,b = b,a
    xau = list(input().split())
    number1 = list(xau[0])
    if (len(xau) < 2): number2 = list(input())
    else : number2 = list(xau[1])
    print(cd(number1,number2,b,a),cd(number1,number2,a,b))