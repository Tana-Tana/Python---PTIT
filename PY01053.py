if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = int(input())
        if number % 3 ==0: print("YES")
        else: print("NO")
        