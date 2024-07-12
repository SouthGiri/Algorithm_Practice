import sys
input = sys.stdin.readline

def solve(n, k):
    def place(d):
        cnt = 1
        last_pos = 0
        for i in range(1, k):
            nxt = last_pos + d
            if nxt >= n:
                return False
            last_pos = nxt
            cnt += 1
        return cnt >= k

    low, high = 1, n
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if place(mid):
            best = mid
            low = mid+1
        else:
            high = mid-1
    return best


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 2:
        print(n-k)
    elif k == n:
        print(0)
    else:
        print(solve(n, k) - 1)