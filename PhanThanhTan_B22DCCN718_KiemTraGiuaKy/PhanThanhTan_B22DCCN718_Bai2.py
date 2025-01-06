from itertools import combinations


def longest_increasing_subsequence(arr):  # Tìm độ dài dãy con tăng dài nhất
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] >= arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# Tìm tất cả các dãy con không giảm có độ dài k
def all_non_decreasing_subsequences(arr, k):
    n = len(arr)
    subsequences = []

    for comb in combinations(arr, n - k):
        if list(comb) == sorted(comb):
            subsequences.append(list(comb))

    return subsequences


def find_min_k(arr):  # Tìm giá trị k nhỏ nhất và tất cả các phương án có thể
    n = len(arr)
    lis_length = longest_increasing_subsequence(arr)
    k = n - lis_length

    subsequences = all_non_decreasing_subsequences(arr, k)

    return k, subsequences


arr = input().split()
k, subsequences = find_min_k(arr)

print("K =", k)
print("Các phương án có thể là:")
for seq in subsequences:
    print(seq)
