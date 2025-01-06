def Check(number):
    number_list = [int(digit) for digit in str(abs(number))]
    # print(number_list)
    if sum(number_list)%10 !=0: return False

    for i in range(len(number_list)-1):
        if abs(number_list[i] - number_list[i+1]) != 2: return False
    return True

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        number = int(input())
        if(Check(number) == True): print("YES")
        else: print("NO")