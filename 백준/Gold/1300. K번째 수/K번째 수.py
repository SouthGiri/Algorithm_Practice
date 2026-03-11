import sys
input = sys.stdin.readline


N = int(input())
K = int(input())

ans = 0
left, right = 1, K
while left <= right:
    mid = (left + right) // 2

    smaller_nums = 0
    for i in range(1, N+1):
        smaller_nums += min(mid//i, N)
    
    if smaller_nums >= K:
        ans = mid
        right = mid-1
    else:
        left = mid+1

print(ans)