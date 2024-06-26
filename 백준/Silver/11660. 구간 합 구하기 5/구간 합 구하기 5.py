import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = mat[0][0]

for i in range(n):
    for j in range(n):
        if i == 0:
            dp[i][j] = mat[i][j] + dp[i][j-1]
        elif j == 0:
            dp[i][j] = mat[i][j] + dp[i-1][j]
        else:
            dp[i][j] = mat[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 >= 2 and y1 >= 2:
        print(dp[x2-1][y2-1] - dp[x1-2][y2-1] - dp[x2-1][y1-2] + dp[x1-2][y1-2])
    elif x1 >= 2:
        print(dp[x2-1][y2-1] - dp[x1-2][y2-1])
    elif y1 >= 2:
        print(dp[x2-1][y2-1] - dp[x2-1][y1-2])
    else:
        print(dp[x2-1][y2-1])