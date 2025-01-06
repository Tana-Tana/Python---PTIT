def thu_gon_day_so(n, list_n):
    if n == 1: return 1
    if n == 2:
        if (int(list_n[0]) + int(list_n[1]))%2==0: return 0
        else: return 2
    res_list = []
    res_list.append(list_n[0])
    for i in range(1,n):
        if res_list: 
            top_element = int(res_list.pop())
            if (int(list_n[i]) + top_element) % 2 != 0:
                res_list.append(str(top_element))
                res_list.append(list_n[i])
        else: 
            res_list.append(list_n[i])
        
    return len(res_list)


#main
n = int(input())
list_n =  input().split()
print(thu_gon_day_so(n,list_n))
    
    