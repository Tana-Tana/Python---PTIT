direction_res = {}
direction_res[1] = 1
while True:
    check = 0
    arr = []
    for i in direction_res:
        if i < 10**18: # key
            if not((i*2) in direction_res):
                arr.append(i*2)
            if not((i*3) in direction_res):
                arr.append(i*3)
            if not((i*5) in direction_res):
                arr.append(i*5) 
    # them cac phan tu cua mang vao direction
    for i in arr:
        direction_res[i] = 1
        check = 1
    if check == 0: break # neu ma k co phan tu nao trong mang thi break

# set lai gia tri cac cap key - value => vi tri
cnt = 1
arr_direction_sorted = sorted(direction_res)
for i in arr_direction_sorted:
    direction_res[i] = cnt
    cnt+=1

# main
test = int(input())
while test > 0:
    test -= 1
    number = int(input())
    if not( number in direction_res): print("Not in sequence")
    else: print(direction_res[number])