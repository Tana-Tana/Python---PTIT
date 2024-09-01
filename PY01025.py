def Solve(n):
    solve = ""
    cnt = 0
    for i in range(len(n)-1, -1, -1):

        if cnt == 3:
            solve += ","
            cnt = 0
        solve += n[i]
        cnt += 1
    return solve[::-1]


test = input()
print(Solve(test))
