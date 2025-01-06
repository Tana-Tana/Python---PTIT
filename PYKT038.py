
nhi_phan =  input()
if len(nhi_phan) % 3 != 0:
    du = 3 - len(nhi_phan)%3
    while du != 0: nhi_phan = '0' + nhi_phan; du-=1
# print(nhi_phan)
#Tach 3 so
save_list = []
for i in range(0,len(nhi_phan),3):
    save_list.append(nhi_phan[i:i+3])
# print(save_list)
# tinh toan
res = ''
for i in save_list:
    res += str(4*int(i[0]) + 2*int(i[1]) + int(i[2]))
print(res)