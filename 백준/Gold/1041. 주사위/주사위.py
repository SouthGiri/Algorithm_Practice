import sys
input = sys.stdin.readline

from itertools import combinations

N = int(input())
data = list(map(int, input().split()))

three_idx = [[0, 1, 2], [0, 1, 3], [0, 2, 4], [0, 3, 4],
             [1, 2, 5], [1, 3, 5], [2, 4, 5], [3, 4, 5]]
two_index = list(filter(lambda x: sum(x) != 5, combinations(range(6), 2)))

three_val = 1e9
for i, j, k in three_idx:
    tmp = data[i] + data[j] + data[k]
    three_val = min(three_val, tmp)

two_val = 1e9
for i, j in two_index:
    tmp = data[i] + data[j]
    two_val = min(two_val, tmp)

one_val = min(data)

three_count = 4
two_count = 8*N - 12
one_count = (N-2) * (5*N - 6)

if N == 1:
    ans = sum(data) - max(data)
else:
    ans = (three_val * three_count) + \
            (two_val * two_count) + (one_val * one_count)

print(ans)