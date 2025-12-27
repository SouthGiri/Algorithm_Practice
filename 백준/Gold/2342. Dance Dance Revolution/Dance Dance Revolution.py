import sys
input = sys.stdin.readline

INF = 1e9

def move(now, nxt):
    if now == 0:
        return 2
    
    if now == nxt:
        return 1
    elif abs(now-nxt) == 2:
        return 4
    else:
        return 3

command = list(map(int, input().split()))
L = len(command)

dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(L)]
dp[0][0][0] = 0

for i in range(1, L):
    now = command[i-1]
    for left in range(5):
        for right in range(5):
            dp[i][left][now] = min(dp[i][left][now], dp[i-1][left][right] + move(right, now))
            dp[i][now][right] = min(dp[i][now][right], dp[i-1][left][right] + move(left, now))
    
print(min(map(min, dp[L-1])))

