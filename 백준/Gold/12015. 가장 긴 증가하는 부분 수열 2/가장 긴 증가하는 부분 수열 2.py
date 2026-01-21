import sys
input = sys.stdin.readline

from bisect import bisect_left

N = int(input())
data = list(map(int, input().split()))

ans = [data[0]]

for x in data[1:]:
    if x > ans[-1]:
        ans.append(x)
    else:
        idx = bisect_left(ans, x)
        ans[idx] = x

print(len(ans))