def LamTron(number):
    number_list = list(number)
    # lat nguoc chuoi
    number_list = number_list[::-1]
    #kiem tra
    for i in range(len(number_list)-1):
        if int(number_list[i]) >= 5: # kiem tra neu so hien tai >= 5
            number_list[i+1] = str(int(number_list[i+1]) + 1) if (int(number_list[i+1]) != 9 or i+2 == len(number_list)) else number_list[i+1]
        # bien so hien tai thanh so 0
        number_list[i] = 0
    # lat nguoc lai day
    number_list = number_list[::-1]

    #in ra
    for item in number_list:
        print(item,end='')
    print()


if __name__ == '__main__':
    t = int(input()) # nhap test case
    while t > 0:
        t-=1
        number = input() # nhap so can kiem tra
        LamTron(number)
        
    

    
