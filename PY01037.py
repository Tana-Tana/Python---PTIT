from bisect import *
import sys
# array numbers "Phản Nguyên Tố"
nums = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
# sys.stdin.readline() the same input() but fastter and not delete '\n'. At ex, use input() => TLE
# bisect_left use by bisect: return left pos while array remain in startState
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(nums[bisect_left(nums, n)])

# Way to set up array nums
# from array import array
# limit = 10**7
# uocSo = array('I', [0]*(limit+1))
# for i in range(1,limit+1,1):
#     for j in range(i,limit+1,i):
#         uocSo[j] += 1
# print(uocSo)

# nums = []
# for i in range(1,10**7 + 1):
#     sum = 0
#     for j in range(1,i,1):
#         sum += uocSo[j]
#     if uocSo[i] > sum: nums.append(i)

# print(nums)
