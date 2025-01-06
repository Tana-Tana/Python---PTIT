from itertools import product

def generate_strings(n):
    # Tập hợp kết quả
    result = []
    cnt = 0
    # Duyệt độ dài từ 3 đến n (vì có mặt đủ 3 thằng)
    for length in range(3, n + 1):
        # Sinh tất cả các xâu có độ dài length: tổng xâu sinh ra là len({A,B,C})^length
        for s in product({'A','B','C'}, repeat=length):
            s = ''.join(s)
            # Đếm số lượng A, B, C
            count_a = s.count('A')
            count_b = s.count('B')
            count_c = s.count('C')
            # Kiểm tra điều kiện
            if 0 < count_a <= count_b <= count_c:
                result.append(s)
    
    # Trả về danh sách kết quả đã được sắp xếp
    return result

# Đọc input
n = int(input())

# Gọi hàm và in kết quả
strings = generate_strings(n)
strings.sort(key = lambda x: (len(x), x)) # sắp xếp x theo thứ tự từ điển nếu chiều dài bằng nhau, không thì sắp xếp theo chiều dài tăng dần
for s in strings:
    print(s)
