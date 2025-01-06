import pickle
from collections import Counter

# main
with open("DATA1.in", "rb") as file1, open("DATA2.in", "rb") as file2:
    arr1 = pickle.load(file1)
    arr2 = pickle.load(file2)

# Đếm tần suất
dict_arr1 = Counter(map(int, arr1))
dict_arr2 = Counter(map(int, arr2))

# Sắp xếp theo key tăng dần
dict_arr1 = dict(sorted(dict_arr1.items()))
dict_arr2 = dict(sorted(dict_arr2.items()))

# Xác định key có trong cả hai
for key, value in dict_arr1.items():
    if key in dict_arr2:
        print(key, value, dict_arr2[key])
