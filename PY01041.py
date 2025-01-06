def Check(number):
    if len(number) < 3: return False
    check = 0
    for i in range(len(number)):
        list_left = number[:i+1]
        list_right = number[i:]
        checkListLeft = 1
        checkListRight = 1
        for j in range(len(list_left)-1):
            if list_left[j] >= list_left[j+1]:
                checkListLeft = 0
                break
        for j in range(len(list_right)-1):
            if list_right[j] <= list_right[j+1]:
                checkListRight = 0
                break

        if (checkListLeft==1) and (checkListRight==1): 
            check = 1
            break
    if check == 0: return False
    return True


if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        n = input()
        if Check(n) == True: print("YES")
        else: print("NO")