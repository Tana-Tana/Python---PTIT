def check(number):
    number_list = list(number)
    for i in range(len(number_list) - 1):
        if(int(number_list[i]) > int(number_list[i+1])):
            return False
    return True

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = input()
        if check(number) == True: print("YES")
        else: print("NO")