import sys
input = sys.stdin.readline


# 연속된 집은 색이 같으면 안 됨
# dp 

n = int(input())
paint = []
for _ in range(n):
    paint.append(list(map(int, input().split())))

dp = [[0]*3 for _ in range(n)]

dp[0][0], dp[0][1], dp[0][2] = paint[0][0], paint[0][1], paint[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + paint[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + paint[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + paint[i][2]

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))