read_and_listen_list = [0.0, 0.0, 0.0, 2.5, 2.5, 3.0, 3.0, 3.5, 3.5, 3.5, 4.0, 4.0, 4.0, 4.5, 4.5, 4.5, 5.0,5.0,5.0,5.0,5.5,5.5,5.5, 6.0, 6.0, 6.0, 6.0,6.5,6.5,6.5,7.0,7.0,7.0,7.5,7.5, 8.0, 8.0,8.5,8.5,9.0,9.0]

#main
test = int(input())
while test > 0:
    test -=1
    xau = input().split()
    index_reading, index_listening = int(xau[0]), int(xau[1])
    score_s, score_w = float(xau[2]),float(xau[3])
    score_r,score_l = read_and_listen_list[index_reading], read_and_listen_list[index_listening]
    score = (score_l + score_r + score_s + score_w)/4
    
    dec = int(str(score)[:1])
    thap_phan = str(score)[2:4]
    
    if int(thap_phan) < 25: thap_phan = 0
    elif int(thap_phan) < 75: thap_phan = 5
    else:
        dec+=1
        thap_phan = 0
    print(f"{dec}.{thap_phan}")
